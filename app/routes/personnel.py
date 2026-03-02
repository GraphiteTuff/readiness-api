from fastapi import APIRouter
from app.models.personnel import PersonnelCreate

router = APIRouter()

fake_db = []

@router.post("/personnel/")
def create_personnel(person: PersonnelCreate):
    fake_db.append(person)
    return {"message": "Personnel added", "data": person}

@router.get("/personnel/")
def list_personnel():
    return fake_db