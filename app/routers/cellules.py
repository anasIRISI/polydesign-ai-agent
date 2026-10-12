from fastapi import APIRouter, HTTPException

from app.repositories.cellules import (
    get_cellule_by_id,
    search_cellules_by_libelle,
    get_cellules_by_zone,
    get_cellule_effectif,
    get_cellules_by_ressource,
)


router = APIRouter(
    prefix="/cellules",
    tags=["Cellules"]
)


@router.get("/search/{libelle}")
def cellules_by_libelle(libelle: str):
    cellules = search_cellules_by_libelle(libelle)

    return {
        "count": len(cellules),
        "cellules": cellules
    }


@router.get("/zone/{zone}")
def cellules_by_zone(zone: int):
    cellules = get_cellules_by_zone(zone)

    return {
        "count": len(cellules),
        "cellules": cellules
    }


@router.get("/ressource/{ressource}")
def cellules_by_ressource(ressource: str):
    cellules = get_cellules_by_ressource(ressource)

    return {
        "count": len(cellules),
        "cellules": cellules
    }


@router.get("/{cellule_id}/effectif")
def cellule_effectif(cellule_id: int):
    cellule = get_cellule_effectif(cellule_id)

    if cellule is None:
        raise HTTPException(
            status_code=404,
            detail="Cellule introuvable"
        )

    return cellule


@router.get("/{cellule_id}")
def cellule_by_id(cellule_id: int):
    cellule = get_cellule_by_id(cellule_id)

    if cellule is None:
        raise HTTPException(
            status_code=404,
            detail="Cellule introuvable"
        )

    return cellule