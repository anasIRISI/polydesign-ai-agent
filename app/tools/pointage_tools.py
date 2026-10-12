from app.repositories.pointage import (
    get_pointage_by_matricule,
    get_pointage_by_matricule_and_date,
    get_employes_by_cellule_and_date,
    get_employes_by_cellule
)


def rechercher_pointage_employe(matricule: int):
    """
    Donne le pointage d'un employé à partir de son matricule.
    """
    return get_pointage_by_matricule(matricule)


def rechercher_pointage_employe_date(matricule: int, date):
    """
    Donne le pointage d'un employé pour une date donnée.
    """
    return get_pointage_by_matricule_and_date(
        matricule,
        date
    )


def compter_employes_cellule_date(cellule_id: int, date):
    """
    Compte le nombre d'employés ayant pointé dans une cellule
    à une date donnée.
    """
    return get_employes_by_cellule_and_date(
        cellule_id,
        date
    )


def compter_employes_par_cellule(date):
    """
    Donne le nombre d'employés ayant pointé dans chaque cellule
    pour une date donnée.
    """
    return get_employes_by_cellule(date)

