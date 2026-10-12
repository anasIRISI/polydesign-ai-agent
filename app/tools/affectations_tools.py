
from app.repositories.affectations import (
    get_affectations_by_cellule,
    get_affectation_by_matricule,
    get_personnes_by_bloc,
    get_employes_by_bloc,
    get_employes_by_cellule,
    get_employes_by_emplacement,
)


def rechercher_affectations_cellule(cellule_id: int):
    """
    Recherche les affectations associées à une cellule.
    """
    return get_affectations_by_cellule(cellule_id)


def rechercher_affectation_matricule(matricule: int):
    """
    Recherche l'affectation d'un employé à partir de son matricule.
    """
    return get_affectation_by_matricule(matricule)


def rechercher_personnes_bloc(bloc: str):
    """
    Recherche les personnes affectées à un bloc donné.
    """
    return get_personnes_by_bloc(bloc)


def obtenir_employes_par_bloc():
    """
    Retourne le nombre d'employés distincts par bloc,
    classés du plus fréquent au moins fréquent.
    """
    return get_employes_by_bloc()


def obtenir_employes_par_cellule():
    """
    Retourne le nombre d'employés distincts par cellule.
    """
    return get_employes_by_cellule()


def obtenir_employes_par_emplacement():
    """
    Retourne le nombre d'employés distincts par emplacement,
    cellule et bloc.
    """
    return get_employes_by_emplacement()
