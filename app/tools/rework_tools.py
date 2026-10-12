
from app.repositories.rework import (
    get_rework_by_codebarre,
    get_reworks_by_reference,
    get_reworks_by_defaut,
    get_reworks_by_matricule,
    get_reworks_by_date
)


def rechercher_rework_codebarre(codebarre: str):
    """
    Recherche les reworks associés à un code-barres.
    """
    return get_rework_by_codebarre(codebarre)


def rechercher_reworks_reference(reference: str):
    """
    Recherche les reworks associés à une référence.
    """
    return get_reworks_by_reference(reference)


def obtenir_reworks_par_defaut():
    """
    Retourne le nombre de reworks par défaut,
    classés du plus fréquent au moins fréquent.
    """
    return get_reworks_by_defaut()


def rechercher_reworks_operateur(matricule: int):
    """
    Recherche les reworks associés à un opérateur.
    """
    return get_reworks_by_matricule(matricule)


def obtenir_reworks_par_date(date: str):
    """
    Retourne le nombre de reworks pour une date donnée.
    """
    return get_reworks_by_date(date)

