from app.tools.active_carton_ctrl_coiffe_tools import (
    obtenir_cartons_par_reference,
    obtenir_references,
    obtenir_cartons_par_machine,
    obtenir_cartons_par_cellule,
    obtenir_cartons_par_shift,
)

from app.tools.blocages_tools import (
    obtenir_blocages_par_cellule,
    obtenir_blocages_par_cause,
    obtenir_blocages_par_description,
    obtenir_duree_blocages,
    obtenir_temps_total_blocage,
    obtenir_temps_blocage_par_cellule,
)

from app.tools.conformes_tools import (
    obtenir_conformes_par_reference,
)

from app.tools.scrap_tools import (
    obtenir_scraps_par_defaut,
    obtenir_scraps_par_operateur,
    obtenir_scraps_par_date,
    obtenir_scraps_par_reference_et_defaut,
)

from app.tools.rework_tools import (
    obtenir_reworks_par_defaut,
)

from app.tools.carton_tools import (
    obtenir_cartons_complets,
    obtenir_cartons_par_etat,
    obtenir_quantite_par_reference_et_cellule,
    obtenir_production_par_jour,
)


def tester(nom, fonction):
    print("\n" + "=" * 60)
    print(f"TEST : {nom}")
    print("=" * 60)

    try:
        result = fonction()

        print("✅ OK")
        print(f"Type : {type(result).__name__}")

        if isinstance(result, list):
            print(f"Nombre de résultats : {len(result)}")

            for row in result[:3]:
                print(row)

        else:
            print(result)

    except Exception as e:
        print("❌ ERREUR")
        print(type(e).__name__)
        print(str(e))


# ============================================================
# ACTIVE CARTON
# ============================================================

tester(
    "Cartons par référence",
    obtenir_cartons_par_reference
)

tester(
    "Liste des références",
    obtenir_references
)

tester(
    "Cartons par cellule",
    obtenir_cartons_par_cellule
)

tester(
    "Cartons par shift",
    obtenir_cartons_par_shift
)


# ============================================================
# BLOCAGES
# ============================================================

tester(
    "Blocages par cellule",
    obtenir_blocages_par_cellule
)

tester(
    "Blocages par cause",
    obtenir_blocages_par_cause
)

tester(
    "Blocages par description",
    obtenir_blocages_par_description
)

tester(
    "Durée des blocages",
    obtenir_duree_blocages
)

tester(
    "Temps total de blocage",
    obtenir_temps_total_blocage
)

tester(
    "Temps de blocage par cellule",
    obtenir_temps_blocage_par_cellule
)


# ============================================================
# CONFORMES
# ============================================================

tester(
    "Conformes par référence",
    obtenir_conformes_par_reference
)


# ============================================================
# SCRAP
# ============================================================

tester(
    "Scraps par défaut",
    obtenir_scraps_par_defaut
)

tester(
    "Scraps par opérateur",
    obtenir_scraps_par_operateur
)

tester(
    "Scraps par référence et défaut",
    obtenir_scraps_par_reference_et_defaut
)


# ============================================================
# REWORK
# ============================================================

tester(
    "Reworks par défaut",
    obtenir_reworks_par_defaut
)


# ============================================================
# CARTON
# ============================================================

tester(
    "Cartons complets",
    obtenir_cartons_complets
)

tester(
    "Cartons par état",
    obtenir_cartons_par_etat
)

tester(
    "Quantité par référence et cellule",
    obtenir_quantite_par_reference_et_cellule
)

tester(
    "Production par jour",
    obtenir_production_par_jour
)
