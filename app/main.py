from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Readiness API")

class HealthResponse(BaseModel):
    status: str

@app.get("/")
def root():
    return {"status": "Readiness API running"}

@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "ok"}