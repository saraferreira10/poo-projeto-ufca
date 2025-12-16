from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.dados import criar_tabelas

@asynccontextmanager
async def lifespan(_app: FastAPI):
    criar_tabelas()
    yield

app = FastAPI(title="The Catalog API", lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "API rodando 🚀"}