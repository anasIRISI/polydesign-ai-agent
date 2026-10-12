from fastapi import APIRouter

from app.repositories.active_carton_ctrl_coiffe import (
    get_cartons_by_reference,
    get_references,
    get_cartons_by_machine,
    get_cartons_by_machine_count,
    get_cartons_by_cellule,
    get_cartons_by_shift,
)


router = APIRouter(
    prefix="/production",
    tags=["Production / Cartons"]
)


@router.get("/cartons-par-reference")
def cartons_par_reference():
    result = get_cartons_by_reference()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/references")
def references():
    result = get_references()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/cartons-machine/{machine}")
def cartons_machine(machine: str):
    result = get_cartons_by_machine(machine)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/cartons-par-machine")
def cartons_par_machine():
    result = get_cartons_by_machine_count()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/cartons-par-cellule")
def cartons_par_cellule():
    result = get_cartons_by_cellule()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/cartons-par-shift")
def cartons_par_shift():
    result = get_cartons_by_shift()

    return {
        "count": len(result),
        "data": result
    }