
from app.repositories.conformes import (
    get_conformes_by_carton,
    get_conformes_by_reference,
    get_all_conformes_count_by_reference,
    get_conformes_count_by_date,
    get_conformes_count_by_reference,
)


def rechercher_conformes_carton(nticket_carton: int):
    """
    Recherche les pièces conformes associées à un carton.
    """
    return get_conformes_by_carton(nticket_carton)


def rechercher_conformes_reference(reference: str):
    """
    Recherche les pièces conformes associées à une référence.
    """
    return get_conformes_by_reference(reference)


def obtenir_conformes_par_reference():
    """
    Retourne le nombre d'enregistrements conformes
    pour chaque référence, classés par ordre décroissant.
    """
    return get_all_conformes_count_by_reference()


def obtenir_conformes_par_date(date):
    """
    Retourne le nombre de scans conformes pour une date donnée.
    """
    return get_conformes_count_by_date(date)


def obtenir_conformes_reference(reference: str):
    """
    Retourne le nombre de scans conformes pour une référence donnée.
    """
    return get_conformes_count_by_reference(reference)
