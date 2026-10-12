from fastapi import APIRouter
from app.tools.efficience_tools import rechercher_efficience_cellules_date
from app.repositories.efficience_cellule import (
    get_efficience_cellule,
    get_efficience_operateur,
    get_efficience_by_shift,

)


router = APIRouter(
    prefix="/efficience",
    tags=["Efficience"]
)


@router.get("/cellule/{cellule_id}")
def efficience_cellule(
    cellule_id: int,
    date: str
):
    result = get_efficience_cellule(
        cellule_id,
        date
    )

    return {
        "count": len(result),
        "data": result
    }


@router.get("/operateur/{matricule}")
def efficience_operateur(matricule: int):
    result = get_efficience_operateur(matricule)

    return {
        "count": len(result),
        "data": result
    }

@router.get("/cellules/date/{date}")
def efficience_cellules_date(date: str):
    return rechercher_efficience_cellules_date(date)


@router.get("/shift/{shift_id}")
def efficience_shift(
    shift_id: int,
    date: str
):
    result = get_efficience_by_shift(
        shift_id,
        date
    )

    return {
        "count": len(result),
        "data": result
    }