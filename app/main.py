from fastapi import FastAPI
from app.routes import personnel

app = FastAPI()

app.include_router(personnel.router)