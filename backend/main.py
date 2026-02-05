from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
import models, schemas, database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/contacts", response_model=List[schemas.ContactResponse])
def get_contacts(
    search: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(database.get_db)
):
    skip = (page - 1) * limit
    query = db.query(models.Contact)
    
    if search:
        query = query.filter(models.Contact.name.ilike(f"%{search}%") | models.Contact.phone_number.ilike(f"%{search}%"))
    
    contacts = query.offset(skip).limit(limit).all()
    return contacts

@app.post("/contacts", response_model=schemas.ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(database.get_db)):
    db_contact = models.Contact(**contact.model_dump())
    try:
        db.add(db_contact)
        db.commit()
        db.refresh(db_contact)
        return db_contact
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Phone number or Email already exists")

@app.get("/contacts/{id}", response_model=schemas.ContactResponse)
def get_contact(id: int, db: Session = Depends(database.get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.put("/contacts/{id}", response_model=schemas.ContactResponse)
def update_contact(id: int, contact_update: schemas.ContactUpdate, db: Session = Depends(database.get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    update_data = contact_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_contact, key, value)
    
    try:
        db.commit()
        db.refresh(db_contact)
        return db_contact
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Phone number or Email already exists")

@app.delete("/contacts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(id: int, db: Session = Depends(database.get_db)):
    db_contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    db.delete(db_contact)
    db.commit()
    return None
