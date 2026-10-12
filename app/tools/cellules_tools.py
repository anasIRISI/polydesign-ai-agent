
from app.repositories.cellules import (
    get_cellule_by_id,
    search_cellules_by_libelle,
    get_cellules_by_zone,
    get_cellule_effectif,
    get_cellules_by_ressource,
)


def rechercher_cellule(cellule_id: int):
    """
    Recherche une cellule à partir de son identifiant.
    """
    return get_cellule_by_id(cellule_id)


def rechercher_cellules_par_libelle(libelle: str):
    """
    Recherche les cellules correspondant à un libellé.
    """
    return search_cellules_by_libelle(libelle)


def rechercher_cellules_par_zone(zone: int):
    """
    Recherche les cellules appartenant à une zone donnée.
    """
    return get_cellules_by_zone(zone)


def rechercher_effectif_cellule(cellule_id: int):
    """
    Retourne l'effectif d'une cellule donnée.
    """
    return get_cellule_effectif(cellule_id)


def rechercher_cellules_par_ressource(ressource: str):
    """
    Recherche les cellules utilisant une ressource principale donnée.
    """
    return get_cellules_by_ressource(ressource)
