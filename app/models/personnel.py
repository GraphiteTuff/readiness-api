from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class PersonnelCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    rank: Optional[str] = Field(None, max_length=20)
    unit: Optional[str] = Field(None, max_length=120)

class PersonnelUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=120)
    rank: Optional[str] = Field(None, max_length=20)
    unit: Optional[str] = Field(None, max_length=120)

class PersonnelOut(BaseModel):
    id: UUID
    name: str
    rank: Optional[str] = None
    unit: Optional[str] = None