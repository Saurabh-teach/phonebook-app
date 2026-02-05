# Phonebook App

A full-stack CRUD application for managing contacts.

## Stack
- **Backend:** FastAPI, SQLAlchemy, Pydantic, PostgreSQL
- **Frontend:** Vue 3, Vite, Pinia, Axios
- **Infrastructure:** Docker Compose

## Prerequisites
- Docker & Docker Compose
- (Optional) Node.js & Python 3.12 for local development without Docker

## Running with Docker (Recommended)

1. Build and start the services:
   ```bash
   docker compose up --build
   ```

2. Access the application:
   - Frontend: [http://localhost:5173](http://localhost:5173)
   - Backend API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Local Development (Manual)

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. Ensure PostgreSQL is running and update `DATABASE_URL` env var.
4. `uvicorn main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`
