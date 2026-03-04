from fastapi import FastAPI
from app.routes.personnel import router as personnel_router

app = FastAPI(title="Readiness API")

@app.get("/")
def root():
    return {"status": "Readiness API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(personnel_router)