from datetime import date

from fastapi import APIRouter

from app.repositories.carton import (
    get_cartons_by_cellule,
    get_carton_by_number,
    get_total_quantity_by_cellule,
    get_complete_cartons,
    get_cartons_by_state,
    get_quantity_by_reference_and_cellule,
    get_production_by_day,
    get_quantity_by_date,
)


router = APIRouter(
    prefix="/carton",
    tags=["Cartons"]
)


@router.get("/cellule/{cellule_id}")
def cartons_cellule(cellule_id: int):
    result = get_cartons_by_cellule(cellule_id)
    return {"count": len(result), "data": result}


@router.get("/quantite-cellule/{cellule_id}")
def quantite_par_cellule(cellule_id: int):
    result = get_total_quantity_by_cellule(cellule_id)
    return {"count": len(result), "data": result}


@router.get("/complets")
def cartons_complets():
    result = get_complete_cartons()
    return {"count": len(result), "data": result}


@router.get("/par-etat")
def cartons_par_etat():
    result = get_cartons_by_state()
    return {"count": len(result), "data": result}


@router.get("/quantite-reference-cellule")
def quantite_reference_cellule():
    result = get_quantity_by_reference_and_cellule()
    return {"count": len(result), "data": result}


@router.get("/production-par-jour")
def production_par_jour():
    result = get_production_by_day()
    return {"count": len(result), "data": result}


@router.get("/quantite-date/{date}")
def quantite_date(date: date):
    result = get_quantity_by_date(date)
    return {"count": len(result), "data": result}


@router.get("/{nticket_carton}")
def carton_par_numero(nticket_carton: int):
    result = get_carton_by_number(nticket_carton)
    return {"count": len(result), "data": result}