from fastapi import APIRouter
from datetime import date

from app.repositories.scrap import (
    get_scrap_by_codebarre,
    get_scraps_by_reference,
    get_scraps_by_cellule,
    get_scraps_by_defaut,
    get_scraps_by_operateur,
    get_scraps_by_matricule,
    get_scraps_by_date,
    get_scraps_by_reference_and_defaut
)


router = APIRouter(
    prefix="/scrap",
    tags=["Scrap"]
)


@router.get("/codebarre/{codebarre}")
def scrap_codebarre(codebarre: str):
    return get_scrap_by_codebarre(codebarre)


@router.get("/reference/{reference}")
def scraps_reference(reference: str):
    return get_scraps_by_reference(reference)


@router.get("/cellule/{cellule_id}")
def scraps_cellule(cellule_id: int):
    return get_scraps_by_cellule(cellule_id)


@router.get("/par-defaut")
def scraps_par_defaut():
    return get_scraps_by_defaut()


@router.get("/par-operateur")
def scraps_par_operateur():
    return get_scraps_by_operateur()


@router.get("/operateur/{matricule}")
def scraps_operateur(matricule: int):
    return get_scraps_by_matricule(matricule)


@router.get("/date/{date}")
def scraps_date(date: date):
    return get_scraps_by_date(date)


@router.get("/par-reference-defaut")
def scraps_par_reference_defaut():
    return get_scraps_by_reference_and_defaut()