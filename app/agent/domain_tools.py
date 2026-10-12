from app.tools.active_carton_ctrl_coiffe_tools import (
    obtenir_cartons_par_reference,
    obtenir_references,
    rechercher_cartons_machine,
    obtenir_cartons_par_machine,
    obtenir_cartons_par_cellule,
    obtenir_cartons_par_shift,
)

from app.tools.efficience_tools import (
    rechercher_efficience_cellule,
    rechercher_efficience_cellules_date,
    rechercher_efficience_operateur,
    rechercher_efficience_shift,
)

from app.tools.affectations_tools import (
    rechercher_affectations_cellule,
    rechercher_affectation_matricule,
    rechercher_personnes_bloc,
    obtenir_employes_par_bloc,
    obtenir_employes_par_cellule,
    obtenir_employes_par_emplacement,
)

from app.tools.blocages_tools import (
    rechercher_blocages_cellule,
    rechercher_blocages_shift,
    rechercher_blocages_date,
    rechercher_blocages_periode,
    obtenir_blocages_par_cellule,
    obtenir_blocages_par_cause,
    obtenir_blocages_par_description,
    obtenir_duree_blocages,
    obtenir_temps_total_blocage,
    obtenir_temps_blocage_par_cellule,
)

from app.tools.cellules_tools import (
    rechercher_cellule,
    rechercher_cellules_par_libelle,
    rechercher_cellules_par_zone,
    rechercher_effectif_cellule,
    rechercher_cellules_par_ressource,
)

from app.tools.conformes_tools import (
    rechercher_conformes_carton,
    rechercher_conformes_reference,
    obtenir_conformes_par_reference,
    obtenir_conformes_par_date,
    obtenir_conformes_reference,
)

from app.tools.carton_tools import (
    rechercher_cartons_cellule,
    rechercher_carton_numero,
    obtenir_quantite_totale_cellule,
    obtenir_cartons_complets,
    obtenir_cartons_par_etat,
    obtenir_quantite_par_reference_et_cellule,
    obtenir_production_par_jour,
    obtenir_quantite_par_date,
)

from app.tools.pieces_annulee_tools import (
    rechercher_piece_annulee_codebarre,
    rechercher_pieces_annulees_carton,
    obtenir_annulations_par_reference,
    obtenir_annulations_par_date,
    obtenir_resume_annulations_cellule,
)

from app.tools.pointage_tools import (
    rechercher_pointage_employe,
    rechercher_pointage_employe_date,
    compter_employes_cellule_date,
    compter_employes_par_cellule,
)

from app.tools.rework_tools import (
    rechercher_rework_codebarre,
    rechercher_reworks_reference,
    obtenir_reworks_par_defaut,
    rechercher_reworks_operateur,
    obtenir_reworks_par_date,
)

from app.tools.scrap_tools import (
    rechercher_scrap_codebarre,
    rechercher_scraps_reference,
    rechercher_scraps_cellule,
    obtenir_scraps_par_defaut,
    obtenir_scraps_par_operateur,
    rechercher_scraps_operateur,
    obtenir_scraps_par_date,
    obtenir_scraps_par_reference_et_defaut,
)

from app.tools.rag_tools import rechercher_documents
# ============================================================
# CARTONS
# ============================================================

CARTONS_TOOLS = {
    "obtenir_cartons_par_reference":
        obtenir_cartons_par_reference,

    "obtenir_references":
        obtenir_references,

    "rechercher_cartons_machine":
        rechercher_cartons_machine,

    "obtenir_cartons_par_machine":
        obtenir_cartons_par_machine,

    "obtenir_cartons_par_cellule":
        obtenir_cartons_par_cellule,

    "obtenir_cartons_par_shift":
        obtenir_cartons_par_shift,
}


# ============================================================
# EFFICIENCE
# ============================================================

EFFICIENCE_TOOLS = {
    "rechercher_efficience_cellule":
        rechercher_efficience_cellule,

    "rechercher_efficience_cellules_date":
        rechercher_efficience_cellules_date,

    "rechercher_efficience_operateur":
        rechercher_efficience_operateur,

    "rechercher_efficience_shift":
        rechercher_efficience_shift,
}


# ============================================================
# AFFECTATIONS
# ============================================================

AFFECTATIONS_TOOLS = {
    "rechercher_affectations_cellule":
        rechercher_affectations_cellule,

    "rechercher_affectation_matricule":
        rechercher_affectation_matricule,

    "rechercher_personnes_bloc":
        rechercher_personnes_bloc,

    "obtenir_employes_par_bloc":
        obtenir_employes_par_bloc,

    "obtenir_employes_par_cellule":
        obtenir_employes_par_cellule,

    "obtenir_employes_par_emplacement":
        obtenir_employes_par_emplacement,
}


# ============================================================
# CELLULES
# ============================================================

CELLULES_TOOLS = {

    "rechercher_cellule":
        rechercher_cellule,

    "rechercher_cellules_par_libelle":
        rechercher_cellules_par_libelle,

    "rechercher_cellules_par_zone":
        rechercher_cellules_par_zone,

    "rechercher_effectif_cellule":
        rechercher_effectif_cellule,

    "rechercher_cellules_par_ressource":
        rechercher_cellules_par_ressource,
}

# ============================================================
# CONFORMES
# ============================================================

CONFORMES_TOOLS = {

    "rechercher_conformes_carton":
        rechercher_conformes_carton,

    "rechercher_conformes_reference":
        rechercher_conformes_reference,

    "obtenir_conformes_par_reference":
        obtenir_conformes_par_reference,

    "obtenir_conformes_par_date":
        obtenir_conformes_par_date,

    "obtenir_conformes_reference":
        obtenir_conformes_reference,
}

# ============================================================
# Blocages
# ============================================================
BLOCAGES_TOOLS = {

    "rechercher_blocages_cellule": rechercher_blocages_cellule,

    "rechercher_blocages_shift": rechercher_blocages_shift,

    "rechercher_blocages_date": rechercher_blocages_date,

    "rechercher_blocages_periode": rechercher_blocages_periode,

    "obtenir_blocages_par_cellule": obtenir_blocages_par_cellule,

    "obtenir_blocages_par_cause": obtenir_blocages_par_cause,

    "obtenir_blocages_par_description": obtenir_blocages_par_description,

    "obtenir_duree_blocages": obtenir_duree_blocages,

    "obtenir_temps_total_blocage": obtenir_temps_total_blocage,

    "obtenir_temps_blocage_par_cellule": obtenir_temps_blocage_par_cellule,
}


# ============================================================
# CARTON
# ============================================================

CARTON_TOOLS = {

    "rechercher_cartons_cellule":
        rechercher_cartons_cellule,

    "rechercher_carton_numero":
        rechercher_carton_numero,

    "obtenir_quantite_totale_cellule":
        obtenir_quantite_totale_cellule,

    "obtenir_cartons_complets":
        obtenir_cartons_complets,

    "obtenir_cartons_par_etat":
        obtenir_cartons_par_etat,

    "obtenir_quantite_par_reference_et_cellule":
        obtenir_quantite_par_reference_et_cellule,

    "obtenir_production_par_jour":
        obtenir_production_par_jour,

    "obtenir_quantite_par_date":
        obtenir_quantite_par_date,
}

# ============================================================
# PIECES ANNULEES
# ============================================================

PIECES_ANNULEE_TOOLS = {

    "rechercher_piece_annulee_codebarre":
        rechercher_piece_annulee_codebarre,

    "rechercher_pieces_annulees_carton":
        rechercher_pieces_annulees_carton,

    "obtenir_annulations_par_reference":
        obtenir_annulations_par_reference,

    "obtenir_annulations_par_date":
        obtenir_annulations_par_date,

    "obtenir_resume_annulations_cellule":
        obtenir_resume_annulations_cellule,
}


# ============================================================
# POINTAGE
# ============================================================

POINTAGE_TOOLS = {
    "rechercher_pointage_employe": rechercher_pointage_employe,
    "rechercher_pointage_employe_date": rechercher_pointage_employe_date,
    "compter_employes_cellule_date": compter_employes_cellule_date,
    "compter_employes_par_cellule": compter_employes_par_cellule,
}

# ============================================================
# REWORK
# ============================================================

REWORK_TOOLS = {
    "rechercher_rework_codebarre": rechercher_rework_codebarre,
    "rechercher_reworks_reference": rechercher_reworks_reference,
    "obtenir_reworks_par_defaut": obtenir_reworks_par_defaut,
    "rechercher_reworks_operateur": rechercher_reworks_operateur,
    "obtenir_reworks_par_date": obtenir_reworks_par_date,
}

# ============================================================
# SCRAP
# ============================================================

SCRAP_TOOLS = {
    "rechercher_scrap_codebarre": rechercher_scrap_codebarre,
    "rechercher_scraps_reference": rechercher_scraps_reference,
    "rechercher_scraps_cellule": rechercher_scraps_cellule,
    "obtenir_scraps_par_defaut": obtenir_scraps_par_defaut,
    "obtenir_scraps_par_operateur": obtenir_scraps_par_operateur,
    "rechercher_scraps_operateur": rechercher_scraps_operateur,
    "obtenir_scraps_par_date": obtenir_scraps_par_date,
    "obtenir_scraps_par_reference_et_defaut": obtenir_scraps_par_reference_et_defaut,
}

# ============================================================
# RAG
# ============================================================

RAG_TOOLS = {
    "rechercher_documents":
        rechercher_documents,
}


# ============================================================
# TOUS LES DOMAINES
# ============================================================

DOMAIN_TOOLS = {
    "cartons": CARTONS_TOOLS,
    "efficience": EFFICIENCE_TOOLS,
    "affectations": AFFECTATIONS_TOOLS,
    "blocages": BLOCAGES_TOOLS,
    "cellules": CELLULES_TOOLS,
    "conformes": CONFORMES_TOOLS,
    "carton": CARTON_TOOLS,
    "pieces_annulee": PIECES_ANNULEE_TOOLS,
    "pointage": POINTAGE_TOOLS,
    "rework": REWORK_TOOLS,
    "scrap": SCRAP_TOOLS,
    "rag": RAG_TOOLS,

}

def get_tools_for_domains(domains: list[str]) -> dict:
    """
    Retourne uniquement les fonctions correspondant
    aux domaines sélectionnés par le Router.
    """

    selected_tools = {}

    for domain in domains:

        tools = DOMAIN_TOOLS.get(domain, {})

        selected_tools.update(tools)

    return selected_tools