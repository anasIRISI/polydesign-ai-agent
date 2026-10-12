
from app.repositories.scrap import (
    get_scrap_by_codebarre,
    get_scraps_by_reference,
    get_scraps_by_cellule,
    get_scraps_by_defaut,
    get_scraps_by_operateur,
    get_scraps_by_matricule,
    get_scraps_by_date,
    get_scraps_by_reference_and_defaut
)


def rechercher_scrap_codebarre(codebarre: str):
    """
    Recherche les scraps associés à un code-barres.
    """
    return get_scrap_by_codebarre(codebarre)


def rechercher_scraps_reference(reference: str):
    """
    Recherche les scraps associés à une référence.
    """
    return get_scraps_by_reference(reference)


def rechercher_scraps_cellule(cellule_id: int):
    """
    Recherche les scraps associés à une cellule.
    """
    return get_scraps_by_cellule(cellule_id)


def obtenir_scraps_par_defaut():
    """
    Retourne le nombre de scraps par défaut,
    classés du plus fréquent au moins fréquent.
    """
    return get_scraps_by_defaut()


def obtenir_scraps_par_operateur():
    """
    Retourne le nombre de scraps par opérateur,
    classés du plus fréquent au moins fréquent.
    """
    return get_scraps_by_operateur()


def rechercher_scraps_operateur(matricule: int):
    """
    Recherche les scraps associés à un opérateur.
    """
    return get_scraps_by_matricule(matricule)


def obtenir_scraps_par_date(date: str):
    """
    Retourne le nombre de scraps pour une date donnée.
    """
    return get_scraps_by_date(date)


def obtenir_scraps_par_reference_et_defaut():
    """
    Retourne le nombre de scraps par référence et par défaut,
    classés du plus fréquent au moins fréquent.
    """
    return get_scraps_by_reference_and_defaut()

