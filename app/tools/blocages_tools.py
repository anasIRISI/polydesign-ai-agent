
from app.repositories.blocages import (
    get_blocages_by_cellule,
    get_blocages_by_shift,
    get_blocages_by_date,
    get_blocages_between_dates,
    get_blocages_by_cellule_count,
    get_blocages_by_cause,
    get_blocages_by_description,
    get_blocages_duration,
    get_total_blocage_time,
    get_total_blocage_time_by_cellule,
)


def rechercher_blocages_cellule(cellule_id: int):
    """
    Recherche les blocages associés à une cellule.
    """
    return get_blocages_by_cellule(cellule_id)


def rechercher_blocages_shift(shift_id: int):
    """
    Recherche les blocages associés à un shift.
    """
    return get_blocages_by_shift(shift_id)


def rechercher_blocages_date(date):
    """
    Recherche les blocages enregistrés pour une date donnée.
    """
    return get_blocages_by_date(date)


def rechercher_blocages_periode(date_debut, date_fin):
    """
    Recherche les blocages enregistrés entre deux dates.
    """
    return get_blocages_between_dates(date_debut, date_fin)


def obtenir_blocages_par_cellule():
    """
    Retourne le nombre de blocages par cellule,
    classés du plus fréquent au moins fréquent.
    """
    return get_blocages_by_cellule_count()


def obtenir_blocages_par_cause():
    """
    Retourne le nombre de blocages par cause,
    classés du plus fréquent au moins fréquent.
    """
    return get_blocages_by_cause()


def obtenir_blocages_par_description():
    """
    Retourne le nombre de blocages par description,
    classés du plus fréquent au moins fréquent.
    """
    return get_blocages_by_description()


def obtenir_duree_blocages():
    """
    Retourne la durée de chaque blocage en secondes.
    """
    return get_blocages_duration()


def obtenir_temps_total_blocage():
    """
    Retourne le temps total de blocage en secondes.
    """
    return get_total_blocage_time()


def obtenir_temps_blocage_par_cellule():
    """
    Retourne le nombre de blocages et le temps total
    de blocage pour chaque cellule.
    """
    return get_total_blocage_time_by_cellule()
