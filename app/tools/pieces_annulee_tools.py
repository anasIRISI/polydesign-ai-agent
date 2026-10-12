
from app.repositories.pieces_annulee import (
    get_piece_annulee_by_codebarre,
    get_pieces_annulees_by_carton,
    get_annulations_by_reference,
    get_annulations_by_date,
    get_annulation_summary_by_cellule,
)


def rechercher_piece_annulee_codebarre(codebarre: str):
    """
    Recherche une pièce annulée à partir de son code-barres.
    """
    return get_piece_annulee_by_codebarre(codebarre)


def rechercher_pieces_annulees_carton(nticket_carton: int):
    """
    Recherche les pièces annulées associées à un carton.
    """
    return get_pieces_annulees_by_carton(nticket_carton)


def obtenir_annulations_par_reference():
    """
    Retourne le nombre d'annulations par référence.
    """
    return get_annulations_by_reference()


def obtenir_annulations_par_date(date):
    """
    Retourne les annulations pour une date donnée.
    """
    return get_annulations_by_date(date)


def obtenir_resume_annulations_cellule(cellule_id: int):
    """
    Retourne le résumé des annulations pour une cellule.
    """
    return get_annulation_summary_by_cellule(cellule_id)
