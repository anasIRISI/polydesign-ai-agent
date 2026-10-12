from datetime import date

from fastapi import APIRouter

from app.repositories.conformes import (
    get_conformes_by_carton,
    get_conformes_by_reference,
    get_all_conformes_count_by_reference,
    get_conformes_count_by_date,
    get_conformes_count_by_reference,
)


router = APIRouter(
    prefix="/conformes",
    tags=["Conformes"]
)


@router.get("/carton/{nticket_carton}")
def conformes_carton(nticket_carton: int):
    result = get_conformes_by_carton(nticket_carton)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/reference/{reference}")
def conformes_reference(reference: str):
    result = get_conformes_by_reference(reference)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/par-reference")
def conformes_par_reference():
    result = get_all_conformes_count_by_reference()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/par-date/{date}")
def conformes_par_date(date: date):
    result = get_conformes_count_by_date(date)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/scans-reference/{reference}")
def scans_par_reference(reference: str):
    result = get_conformes_count_by_reference(reference)

    return {
        "count": len(result),
        "data": result
    }