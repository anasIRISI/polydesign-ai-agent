from fastapi import FastAPI

from app.routers.cellules import router as cellules_router
from app.routers.efficience_cellule import router as efficience_router
from app.routers.active_carton_ctrl_coiffe import (
    router as production_router
)
from app.routers.affectations import router as affectations_router
from app.routers.blocages import router as blocages_router
from app.routers.carton import router as carton_router
from app.routers.conformes import router as conformes_router
from app.routers.pieces_annulee import router as pieces_annulee_router
from app.routers.pointage import router as pointage_router
from app.routers.rework import router as rework_router
from app.routers.scrap import router as scrap_router
from pydantic import BaseModel
from app.agent.agent import ask_agent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Polydesign AI Agent",
    description="Backend IA pour le système de Polydesign",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str
    session_id: str


@app.post("/chat")
def chat(request: ChatRequest):

    response = ask_agent(
        request.question,
        request.session_id
    )

    return {
        "session_id": request.session_id,
        "question": request.question,
        "response": response
    }


@app.get("/")
def root():
    return {
        "message": "Polydesign AI Agent API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/db-test")
def db_test():
    from sqlalchemy import text
    from app.db.database import engine

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        value = result.scalar()

    return {
        "database": "connected",
        "test": value
    }


app.include_router(cellules_router)
app.include_router(efficience_router)
app.include_router(production_router)
app.include_router(affectations_router)
app.include_router(blocages_router)
app.include_router(carton_router)
app.include_router(conformes_router)
app.include_router(pieces_annulee_router)
app.include_router(pointage_router)
app.include_router(rework_router)
app.include_router(scrap_router)