[![Live API](https://img.shields.io/badge/Live%20API-onrender.com-brightgreen)](https://readiness-api.onrender.com/)
[![Swagger Docs](https://img.shields.io/badge/Docs-Swagger%20UI-blue)](https://readiness-api.onrender.com/docs)

# Readiness API

A lightweight FastAPI service for storing and retrieving **personal readiness records** in a structured, validated format.

- **Framework:** FastAPI (Python)
- **Validation:** Pydantic (request/response models)
- **Docs:** OpenAPI / Swagger UI
- **Run options:** Local dev (uvicorn) or Docker (`8000:8000`)

---

## Table of contents

- [What this is](#what-this-is)
- [Features](#features)
- [API endpoints](#api-endpoints)
- [Quickstart](#quickstart)
  - [Run with Docker](#run-with-docker)
  - [Run locally](#run-locally)
- [Request/response examples](#requestresponse-examples)
- [Project structure](#project-structure)
- [Development](#development)
- [Roadmap](#roadmap)
- [License](#license)

---

## What this is

Readiness API provides a small, production-minded backend that:
1. accepts readiness-related inputs,
2. validates them using strict schemas,
3. persists them (or passes them to a persistence layer),
4. returns consistent, typed responses.



## Project Purpose

Readiness API is a RESTful service designed to manage personnel readiness records in a structured and validated manner.

The system is intentionally built using layered architecture principles to simulate real-world backend engineering patterns used in production environments.

## Features

- ✅ Schema-first design (Pydantic models for inputs/outputs)
- ✅ Consistent JSON responses and error handling
- ✅ Health check endpoint for deployments
- ✅ Interactive API docs (Swagger + ReDoc)
- ✅ Docker-friendly (single port: `8000`)

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
├─ app/
│  ├─ main.py              # FastAPI app entrypoint
│  ├─ api/                 # Routers (endpoints)
│  ├─ models/              # Pydantic models (schemas)
│  ├─ services/            # Business logic
│  └─ storage/             # Persistence adapters (optional)
├─ tests/
├─ Dockerfile
├─ requirements.txt
└─ README.md

---

## Design Principles

- Separation of concerns
- Typed request validation via **Pydantic**
- Modular router pattern
- Extensible data layer design
- Self-documenting OpenAPI schema generation

---

## API Endpoints
Adjust route names below if your implementation differs.

| Method | Route           | Description               |
| -----: | --------------- | ------------------------- |
|    GET | `/`             | Service info              |
|    GET | `/health`       | Health check              |
|   POST | `/records`      | Create a readiness record |
|    GET | `/records/{id}` | Get a record by id        |
|    GET | `/docs`         | Swagger UI                |
|    GET | `/redoc`        | ReDoc                     |


---
## Quickstart

### Run with Docker

**Build the image:**
```bash
docker build -t readiness-api .

## Live Deployment

- **Live API:** [readiness-api.onrender.com](https://readiness-api.onrender.com/)
- **Swagger Docs:** [/docs](https://readiness-api.onrender.com/docs)
- **Health:** [/health](https://readiness-api.onrender.com/health)

### Health Check

**GET /health**

Returns `{"status": "ok"}` when the service is healthy.

---

### Create Personnel Record

**POST /personnel/**

Creates a new personnel readiness record.

#### Request Body

```json
{ "status": "ok" }

```
curl http://localhost:8000/health

Requests are validated against a strongly-typed **Pydantic schema** before processing.

## Running the Application

### Run with Docker

Build the image:

```bash




Author

Jason Graff
Backend-focused software engineering student at Penn State building production-style backend systems with Python and FastAPI.
