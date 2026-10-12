from datetime import date

from fastapi import APIRouter

from app.repositories.blocages import (
    get_blocages_by_cellule,
    get_blocages_by_shift,
    get_blocages_by_date,
    get_blocages_between_dates,
    get_blocages_by_cellule_count,
    get_blocages_by_cause,
    get_blocages_by_description,
    get_blocages_duration,
    get_total_blocage_time,
    get_total_blocage_time_by_cellule,
)


router = APIRouter(
    prefix="/blocages",
    tags=["Blocages"]
)


@router.get("/cellule/{cellule_id}")
def blocages_cellule(cellule_id: int):
    result = get_blocages_by_cellule(cellule_id)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/shift/{shift_id}")
def blocages_shift(shift_id: int):
    result = get_blocages_by_shift(shift_id)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/date/{date}")
def blocages_date(date: date):
    result = get_blocages_by_date(date)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/entre-dates")
def blocages_entre_dates(
    date_debut: date,
    date_fin: date
):
    result = get_blocages_between_dates(
        date_debut,
        date_fin
    )

    return {
        "count": len(result),
        "data": result
    }


@router.get("/par-cellule")
def blocages_par_cellule():
    result = get_blocages_by_cellule_count()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/par-cause")
def blocages_par_cause():
    result = get_blocages_by_cause()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/par-description")
def blocages_par_description():
    result = get_blocages_by_description()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/durees")
def durees_blocages():
    result = get_blocages_duration()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/temps-total")
def temps_total_blocage():
    result = get_total_blocage_time()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/temps-total-par-cellule")
def temps_total_par_cellule():
    result = get_total_blocage_time_by_cellule()

    return {
        "count": len(result),
        "data": result
    }