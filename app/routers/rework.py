from fastapi import APIRouter
from datetime import date

from app.repositories.rework import (
    get_rework_by_codebarre,
    get_reworks_by_reference,
    get_reworks_by_defaut,
    get_reworks_by_matricule,
    get_reworks_by_date
)


router = APIRouter(
    prefix="/rework",
    tags=["Rework"]
)


@router.get("/codebarre/{codebarre}")
def rework_codebarre(codebarre: str):
    return get_rework_by_codebarre(codebarre)


@router.get("/reference/{reference}")
def rework_reference(reference: str):
    return get_reworks_by_reference(reference)


@router.get("/par-defaut")
def reworks_par_defaut():
    return get_reworks_by_defaut()


@router.get("/operateur/{matricule}")
def reworks_operateur(matricule: int):
    return get_reworks_by_matricule(matricule)


@router.get("/date/{date}")
def reworks_date(date: date):
    return get_reworks_by_date(date)