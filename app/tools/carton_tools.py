
from app.repositories.carton import (
    get_cartons_by_cellule,
    get_carton_by_number,
    get_total_quantity_by_cellule,
    get_complete_cartons,
    get_cartons_by_state,
    get_quantity_by_reference_and_cellule,
    get_production_by_day,
    get_quantity_by_date,
)


def rechercher_cartons_cellule(cellule_id: int):
    """
    Recherche les cartons associés à une cellule.
    """
    return get_cartons_by_cellule(cellule_id)


def rechercher_carton_numero(nticket_carton: int):
    """
    Recherche un carton à partir de son numéro de ticket.
    """
    return get_carton_by_number(nticket_carton)


def obtenir_quantite_totale_cellule(cellule_id: int):
    """
    Retourne la quantité totale produite dans une cellule
    à partir des quantités enregistrées dans les cartons.
    """
    return get_total_quantity_by_cellule(cellule_id)


def obtenir_cartons_complets():
    """
    Retourne les cartons ayant l'état 'complet'.
    """
    return get_complete_cartons()


def obtenir_cartons_par_etat():
    """
    Retourne le nombre de cartons par état.
    """
    return get_cartons_by_state()


def obtenir_quantite_par_reference_et_cellule():
    """
    Retourne la quantité totale et le nombre de cartons
    pour chaque référence et chaque cellule.
    """
    return get_quantity_by_reference_and_cellule()


def obtenir_production_par_jour():
    """
    Retourne la production quotidienne avec la quantité totale
    et le nombre de cartons.
    """
    return get_production_by_day()


def obtenir_quantite_par_date(date):
    """
    Retourne la quantité totale et le nombre de cartons
    pour une date donnée.
    """
    return get_quantity_by_date(date)
