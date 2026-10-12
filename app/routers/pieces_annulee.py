from datetime import date

from fastapi import APIRouter

from app.repositories.pieces_annulee import (
    get_piece_annulee_by_codebarre,
    get_pieces_annulees_by_carton,
    get_annulations_by_reference,
    get_annulations_by_date,
    get_annulation_summary_by_cellule,
)


router = APIRouter(
    prefix="/pieces-annulees",
    tags=["Pièces annulées"]
)


@router.get("/piece/{codebarre}")
def piece_annulee(codebarre: str):
    result = get_piece_annulee_by_codebarre(codebarre)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/carton/{nticket_carton}")
def pieces_annulees_carton(nticket_carton: int):
    result = get_pieces_annulees_by_carton(nticket_carton)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/par-reference")
def annulations_par_reference():
    result = get_annulations_by_reference()

    return {
        "count": len(result),
        "data": result
    }


@router.get("/par-date/{date}")
def annulations_par_date(date: date):
    result = get_annulations_by_date(date)

    return {
        "count": len(result),
        "data": result
    }


@router.get("/resume-cellule/{cellule_id}")
def resume_annulations_cellule(cellule_id: int):
    result = get_annulation_summary_by_cellule(cellule_id)

    return {
        "count": len(result),
        "data": result
    }