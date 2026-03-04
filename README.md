[![Live API](https://img.shields.io/badge/Live%20API-onrender.com-brightgreen)](https://readiness-api.onrender.com/)
[![Swagger Docs](https://img.shields.io/badge/Docs-Swagger%20UI-blue)](https://readiness-api.onrender.com/docs)

# Readiness API

A modular backend service built with **FastAPI** that models personnel readiness data using schema-driven validation and clean architectural separation.

This project demonstrates **production-oriented backend API design**, typed request validation, structured routing, and extensible system design using Python.

---

## Project Purpose

Readiness API is a RESTful service designed to manage personnel readiness records in a structured and validated manner.

The system is intentionally built using layered architecture principles to simulate real-world backend engineering patterns used in production environments.

### Key Focus Areas

- Clean separation of concerns
- Strong typing and validation
- Modular routing design
- Extensible persistence layer
- Self-documenting API schemas

---

## Technology Stack

| Layer | Technology |
|------|------------|
| Web Framework | FastAPI |
| Validation | Pydantic |
| ASGI Server | Uvicorn |
| Language | Python 3.12+ |
| API Documentation | OpenAPI (auto-generated) |
| Environment | Python Virtual Environment (venv) |

---

## Architecture Overview

The application follows a layered architecture separating configuration, routing, and domain models.

readiness-api/
│
├── app/
│ ├── main.py
│ ├── models/
│ │ └── personnel.py
│ ├── routes/
│ │ └── personnel.py
│ └── database/
│
├── requirements.txt
└── README.md

---

## Design Principles

- Separation of concerns
- Typed request validation via **Pydantic**
- Modular router pattern
- Extensible data layer design
- Self-documenting OpenAPI schema generation

---

## API Endpoints

## Live Deployment

- **Live API:** https://readiness-api.onrender.com/
- **Swagger Docs:** https://readiness-api.onrender.com/docs
- **Health:** https://readiness-api.onrender.com/health

### Health Check

**GET /health**

Returns `{"status": "ok"}` when the service is healthy.

---

### Create Personnel Record

**POST /personnel/**

Creates a new personnel readiness record.

#### Request Body

```json
{
  "name": "Jason Graff",
  "unit": "JBMDL",
  "certification_status": "GREEN"
}
```
Requests are validated against a strongly-typed **Pydantic schema** before processing.

Running the Application
Build the image:

```bash
docker build -t readiness-api .
Create a virtual environment

python -m venv venv

Activate environment (PowerShell)

venv\Scripts\Activate.ps1

Install dependencies

pip install -r requirements.txt

Start development server

uvicorn app.main:app --reload

Access interactive documentation

http://127.0.0.1:8000/docs
Development Workflow

Models define strict request/response schemas

Routes implement endpoint behavior

Main application registers modular routers

FastAPI auto-generates OpenAPI documentation

Uvicorn runs the ASGI application

Roadmap

Planned enhancements include:

PostgreSQL integration

SQLAlchemy ORM layer

Full CRUD operations

JWT authentication

Unit and integration testing (pytest)

Docker containerization

Cloud deployment (AWS / GCP / Azure)

CI/CD pipeline integration

Why This Project Matters

This project demonstrates:

Backend service architecture

Type-safe API design

Production-aligned folder structure

Modular system expansion strategy

Schema-first API development

These are foundational backend engineering practices used in scalable service design.

Author

Jason Graff
Backend-focused software engineering student at Penn State building production-style backend systems with Python and FastAPI.
