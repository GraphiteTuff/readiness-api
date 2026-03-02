from pydantic import BaseModel

class PersonnelCreate(BaseModel):
    name: str
    unit: str
    certification_status: str