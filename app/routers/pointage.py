from fastapi import APIRouter
from datetime import date

from app.repositories.pointage import (
    get_pointage_by_matricule,
    get_pointage_by_matricule_and_date,
    get_employes_by_cellule_and_date,
    get_employes_by_cellule
)

router = APIRouter(
    prefix="/pointage",
    tags=["Pointage"]
)


@router.get("/employe/{matricule}")
def pointage_employe(matricule: int):
    return get_pointage_by_matricule(matricule)


@router.get("/employe/{matricule}/date/{date}")
def pointage_employe_date(
    matricule: int,
    date: date
):
    return get_pointage_by_matricule_and_date(
        matricule,
        date
    )


@router.get("/cellule/{cellule_id}/employes")
def employes_cellule(
    cellule_id: int,
    date: date
):
    return get_employes_by_cellule_and_date(
        cellule_id,
        date
    )


@router.get("/employes-par-cellule")
def employes_par_cellule(date: date):
    return get_employes_by_cellule(date)