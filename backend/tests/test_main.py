import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database import Base, get_db

# Setup the test database (In-memory SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_contact():
    response = client.post(
        "/contacts",
        json={"name": "Test User", "phone_number": "+1234567890", "email": "test@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert "id" in data

def test_get_contacts():
    # Create one first
    client.post("/contacts", json={"name": "User 1", "phone_number": "1111111111"})
    
    response = client.get("/contacts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "User 1"

def test_get_specific_contact():
    create_res = client.post("/contacts", json={"name": "User 2", "phone_number": "2222222222"})
    contact_id = create_res.json()["id"]
    
    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "User 2"

def test_update_contact():
    create_res = client.post("/contacts", json={"name": "User 3", "phone_number": "3333333333"})
    contact_id = create_res.json()["id"]
    
    response = client.put(f"/contacts/{contact_id}", json={"name": "Updated User"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"

def test_delete_contact():
    create_res = client.post("/contacts", json={"name": "User 4", "phone_number": "4444444444"})
    contact_id = create_res.json()["id"]
    
    response = client.delete(f"/contacts/{contact_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    get_res = client.get(f"/contacts/{contact_id}")
    assert get_res.status_code == 404
