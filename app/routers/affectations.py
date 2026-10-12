from fastapi import APIRouter

from app.repositories.affectations import (
    get_affectations_by_cellule,
    get_affectation_by_matricule,
    get_personnes_by_bloc,
    get_employes_by_bloc,
    get_employes_by_cellule,
    get_employes_by_emplacement,
)


router = APIRouter(
    prefix="/affectations",
    tags=["Affectations"]
)


@router.get("/cellule/{cellule_id}")
def affectations_cellule(cellule_id: int):
    result = get_affectations_by_cellule(cellule_id)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/employe/{matricule}")
def affectation_employe(matricule: int):
    result = get_affectation_by_matricule(matricule)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/bloc/{bloc}")
def personnes_bloc(bloc: str):
    result = get_personnes_by_bloc(bloc)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/employes-par-bloc")
def employes_par_bloc():
    result = get_employes_by_bloc()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/employes-par-cellule")
def employes_par_cellule():
    result = get_employes_by_cellule()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/employes-par-emplacement")
def employes_par_emplacement():
    result = get_employes_by_emplacement()

    return {
        "count": len(result),
        "data": result
    }