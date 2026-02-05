# 📇 Phonebook App

A modern, full-stack Contact Management System built with **FastAPI**, **Vue.js 3**, and **PostgreSQL**. This project demonstrates a complete development lifecycle, including containerization with Docker and CI/CD with GitHub Actions.

---

## ✨ Features
- **Full CRUD Operations**: Create, view, update, and delete contacts with ease.
- **Smart Validation**: Real-time validation for phone numbers, emails (optional), and mandatory fields.
- **Modern UI**: A responsive, clean interface using Vue 3, Vite, and Pinia for state management.
- **Robust Backend**: Fast and safe RESTful API powered by FastAPI and SQLAlchemy.
- **Database Consistency**: PostgreSQL for reliable, persistent data storage.
- **Testing Suite**: Automated unit tests for both Backend (Pytest) and Frontend (Vitest).
- **CI/CD Integrated**: Automated testing on every push via GitHub Actions.

---

## 🛠️ Tech Stack
- **Backend**: Python 3.10+, FastAPI, SQLAlchemy, PostgreSQL, Pydantic.
- **Frontend**: Vue.js 3, Vite, Pinia, Axios.
- **DevOps**: Docker, Docker Compose, GitHub Actions.

---

## 🚀 Getting Started with Docker (Fastest)

Run the entire application (including the database) inside isolated containers:

1. **Clone the repository** (if not already done).
2. **Launch with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
3. **Open your browser**:
   - **App**: [http://localhost:5173](http://localhost:5173)
   - **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 💻 Local Development Setup

If you prefer to run the components manually on your machine:

### 1. Prerequisites
- **Python 3.10+**
- **Node.js 20+**
- **PostgreSQL Server** (e.g., v16)

### 2. Backend (FastAPI)
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
*Note: Update `database.py` with your local PostgreSQL credentials.*

### 3. Frontend (Vue 3)
```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Testing

We ensure quality through comprehensive automated testing.

### Backend Unit Tests
Powered by **Pytest** and **Httpx**. Covers API logic and CRUD flows.
```bash
cd backend
python -m pytest
```

### Frontend Unit Tests
Powered by **Vitest** and **Vue Test Utils**. Covers component rendering and state logic.
```bash
cd frontend
npm run test:unit
```

---

## 📦 Project Deliverables
- `backend/`: FastAPI source code, models, and migrations.
- `frontend/`: Vue 3 components, store, and tests.
- `docker-compose.yml`: Multi-service orchestration.
- `.github/workflows/`: CI/CD automation logic.
- `README.md`: This comprehensive guide.

---

## 💡 Implementation Hints Used
- **Postman/cURL Friendly**: The backend is designed for easy testing via Swagger UI (`/docs`).
- **Official Images**: Docker setup uses `python:3.12-slim`, `node:20-alpine`, and `postgres:16-alpine`.
- **Modern Tooling**: Project scaffolded with Vite for lightning-fast frontend development.
