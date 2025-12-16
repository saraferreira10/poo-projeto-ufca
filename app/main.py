from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import create_db_and_tables

@asynccontextmanager
async def lifespan(_app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="The Catalog API", lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "API rodando 🚀"}
