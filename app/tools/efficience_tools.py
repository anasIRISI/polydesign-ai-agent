
from app.repositories.efficience_cellule import (
    get_efficience_cellule,
    get_efficience_cellules_date,
    get_efficience_operateur,
    get_efficience_by_shift
)


def rechercher_efficience_cellule(cellule_id: int, date: str):
    """
    Recherche l'efficience d'une cellule pour une date donnée.
    """
    return get_efficience_cellule(
        cellule_id,
        date
    )


def rechercher_efficience_cellules_date(date: str):
    """
    Recherche l'efficience de toutes les cellules
    pour une date donnée.
    """
    return get_efficience_cellules_date(date)


def rechercher_efficience_operateur(matricule: int):
    """
    Recherche l'efficience d'un opérateur à partir de son matricule.
    """
    return get_efficience_operateur(matricule)


def rechercher_efficience_shift(shift_id: int, date: str):
    """
    Recherche l'efficience d'un shift pour une date donnée.
    """
    return get_efficience_by_shift(
        shift_id,
        date
    )
