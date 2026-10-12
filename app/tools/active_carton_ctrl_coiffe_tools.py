
from app.repositories.active_carton_ctrl_coiffe import (
    get_cartons_by_reference,
    get_references,
    get_cartons_by_machine,
    get_cartons_by_machine_count,
    get_cartons_by_cellule,
    get_cartons_by_shift,
)


def obtenir_cartons_par_reference():
    """
    Retourne le nombre de cartons uniques par référence,
    classés du plus grand au plus petit nombre.
    """
    return get_cartons_by_reference()


def obtenir_references():
    """
    Retourne la liste des références disponibles.
    """
    return get_references()


def rechercher_cartons_machine(machine: str):
    """
    Recherche les cartons enregistrés par une machine donnée.
    """
    return get_cartons_by_machine(machine)


def obtenir_cartons_par_machine():
    """
    Retourne le nombre de cartons enregistrés par machine,
    classés du plus grand au plus petit nombre.
    """
    return get_cartons_by_machine_count()


def obtenir_cartons_par_cellule():
    """
    Retourne le nombre de cartons uniques par cellule,
    classés du plus grand au plus petit nombre.
    """
    return get_cartons_by_cellule()


def obtenir_cartons_par_shift():
    """
    Retourne le nombre de cartons uniques par shift.
    """
    return get_cartons_by_shift()
