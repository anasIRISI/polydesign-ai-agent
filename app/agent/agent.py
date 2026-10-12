from app.llm.gemini import client
import time
from app.agent.router import detect_domains
from app.agent.domain_tools import get_tools_for_domains

conversation_memory = {}

# =========================
# IMPORT DES TOOLS
# =========================

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

from app.tools.rag_tools import (
    rechercher_documents,
)
# ============================================================
# 1. TOUS LES TOOLS DISPONIBLES POUR L'AGENT
# ============================================================

TOOLS = {

    # -------------------------
    # CARTONS
    # -------------------------

    "obtenir_cartons_par_reference": obtenir_cartons_par_reference,

    "obtenir_references": obtenir_references,

    "rechercher_cartons_machine": rechercher_cartons_machine,

    "obtenir_cartons_par_machine": obtenir_cartons_par_machine,

    "obtenir_cartons_par_cellule": obtenir_cartons_par_cellule,

    "obtenir_cartons_par_shift": obtenir_cartons_par_shift,


    # -------------------------
    # EFFICIENCE
    # -------------------------

    "rechercher_efficience_cellule": rechercher_efficience_cellule,

    "rechercher_efficience_cellules_date": rechercher_efficience_cellules_date,

    "rechercher_efficience_operateur": rechercher_efficience_operateur,

    "rechercher_efficience_shift": rechercher_efficience_shift,


    # -------------------------
    # AFFECTATIONS
    # -------------------------

    "rechercher_affectations_cellule": rechercher_affectations_cellule,

    "rechercher_affectation_matricule": rechercher_affectation_matricule,

    "rechercher_personnes_bloc": rechercher_personnes_bloc,

    "obtenir_employes_par_bloc": obtenir_employes_par_bloc,

    "obtenir_employes_par_cellule": obtenir_employes_par_cellule,

    "obtenir_employes_par_emplacement": obtenir_employes_par_emplacement,

    # -------------------------
    # BLOCAGES
    # -------------------------

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

    # Cellules
    "rechercher_cellule": rechercher_cellule,
    "rechercher_cellules_par_libelle": rechercher_cellules_par_libelle,
    "rechercher_cellules_par_zone": rechercher_cellules_par_zone,
    "rechercher_effectif_cellule": rechercher_effectif_cellule,
    "rechercher_cellules_par_ressource": rechercher_cellules_par_ressource,


    # Conformes

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


    # Carton

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


    # Pieces annulées

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

    
    # pointage

"rechercher_pointage_employe": rechercher_pointage_employe,
"rechercher_pointage_employe_date": rechercher_pointage_employe_date,
"compter_employes_cellule_date": compter_employes_cellule_date,
"compter_employes_par_cellule": compter_employes_par_cellule,

    #REWORK

"rechercher_rework_codebarre": rechercher_rework_codebarre,
"rechercher_reworks_reference": rechercher_reworks_reference,
"obtenir_reworks_par_defaut": obtenir_reworks_par_defaut,
"rechercher_reworks_operateur": rechercher_reworks_operateur,
"obtenir_reworks_par_date": obtenir_reworks_par_date,


#SCRAP

"rechercher_scrap_codebarre": rechercher_scrap_codebarre,
"rechercher_scraps_reference": rechercher_scraps_reference,
"rechercher_scraps_cellule": rechercher_scraps_cellule,
"obtenir_scraps_par_defaut": obtenir_scraps_par_defaut,
"obtenir_scraps_par_operateur": obtenir_scraps_par_operateur,
"rechercher_scraps_operateur": rechercher_scraps_operateur,
"obtenir_scraps_par_date": obtenir_scraps_par_date,
"obtenir_scraps_par_reference_et_defaut": obtenir_scraps_par_reference_et_defaut,

#RAG

"rechercher_documents":
    rechercher_documents,
}



# ============================================================
# 2. DEFINITIONS DES TOOLS POUR GEMINI
# ============================================================

GEMINI_TOOL_DEFINITIONS = {

    # ========================================================
    # CARTONS
    # ========================================================

    "obtenir_cartons_par_reference": {
        "type": "function",
        "name": "obtenir_cartons_par_reference",
        "description": (
            "Retourne le nombre de cartons uniques pour chaque référence."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    "obtenir_references": {
        "type": "function",
        "name": "obtenir_references",
        "description": (
            "Retourne la liste des références disponibles."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    "rechercher_cartons_machine": {
        "type": "function",
        "name": "rechercher_cartons_machine",
        "description": (
            "Recherche les cartons enregistrés par une machine donnée."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "machine": {
                    "type": "string",
                    "description": "Adresse ou identifiant de la machine.",
                }
            },
            "required": ["machine"],
        },
    },

    "obtenir_cartons_par_machine": {
        "type": "function",
        "name": "obtenir_cartons_par_machine",
        "description": (
            "Retourne le nombre de cartons enregistrés par machine."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    "obtenir_cartons_par_cellule": {
        "type": "function",
        "name": "obtenir_cartons_par_cellule",
        "description": (
            "Retourne le nombre de cartons uniques par cellule."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    "obtenir_cartons_par_shift": {
        "type": "function",
        "name": "obtenir_cartons_par_shift",
        "description": (
            "Retourne le nombre de cartons uniques par shift."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },


    # ========================================================
    # EFFICIENCE
    # ========================================================

    "rechercher_efficience_cellule": {
        "type": "function",
        "name": "rechercher_efficience_cellule",
        "description": (
            "Recherche les données d'efficience d'une cellule "
            "pour une date donnée."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "cellule_id": {
                    "type": "integer",
                    "description": "Identifiant de la cellule.",
                },
                "date": {
                    "type": "string",
                    "description": "Date au format YYYY-MM-DD.",
                },
            },
            "required": ["cellule_id", "date"],
        },
    },

    "rechercher_efficience_cellules_date": {
        "type": "function",
        "name": "rechercher_efficience_cellules_date",
        "description": (
            "Recherche les données d'efficience de toutes les cellules "
            "pour une date donnée."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Date au format YYYY-MM-DD.",
                }
            },
            "required": ["date"],
        },
    },

    "rechercher_efficience_operateur": {
        "type": "function",
        "name": "rechercher_efficience_operateur",
        "description": (
            "Recherche les données d'efficience d'un opérateur."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "matricule": {
                    "type": "integer",
                    "description": "Matricule de l'opérateur.",
                }
            },
            "required": ["matricule"],
        },
    },

    "rechercher_efficience_shift": {
        "type": "function",
        "name": "rechercher_efficience_shift",
        "description": (
            "Recherche l'efficience d'un shift pour une date donnée."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "shift_id": {
                    "type": "integer",
                    "description": "Identifiant du shift.",
                },
                "date": {
                    "type": "string",
                    "description": "Date au format YYYY-MM-DD.",
                },
            },
            "required": ["shift_id", "date"],
        },
    },

     # -------------------------
        # BLOCAGES
     # -------------------------
"rechercher_blocages_cellule": {
    "type": "function",
    "name": "rechercher_blocages_cellule",
    "description": (
        "Recherche les blocages associés à une cellule donnée."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "cellule_id": {
                "type": "integer",
                "description": "Identifiant de la cellule."
            }
        },
        "required": ["cellule_id"],
    },
},

"rechercher_blocages_shift": {
    "type": "function",
    "name": "rechercher_blocages_shift",
    "description": (
        "Recherche les blocages associés à un shift donné."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "shift_id": {
                "type": "integer",
                "description": "Identifiant du shift."
            }
        },
        "required": ["shift_id"],
    },
},

"rechercher_blocages_shift": {
    "type": "function",
    "name": "rechercher_blocages_shift",
    "description": (
        "Recherche les blocages associés à un shift donné."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "shift_id": {
                "type": "integer",
                "description": "Identifiant du shift."
            }
        },
        "required": ["shift_id"],
    },
},

"rechercher_blocages_periode": {
    "type": "function",
    "name": "rechercher_blocages_periode",
    "description": (
        "Recherche les blocages enregistrés entre deux dates."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "date_debut": {
                "type": "string",
                "description": "Date de début au format YYYY-MM-DD."
            },
            "date_fin": {
                "type": "string",
                "description": "Date de fin au format YYYY-MM-DD."
            }
        },
        "required": ["date_debut", "date_fin"],
    },
},

"obtenir_blocages_par_cellule": {
    "type": "function",
    "name": "obtenir_blocages_par_cellule",
    "description": (
        "Retourne le nombre de blocages par cellule, "
        "classés du plus fréquent au moins fréquent."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
},

"obtenir_blocages_par_cause": {
    "type": "function",
    "name": "obtenir_blocages_par_cause",
    "description": (
        "Retourne le nombre de blocages par cause, "
        "classés du plus fréquent au moins fréquent."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
},

"obtenir_blocages_par_description": {
    "type": "function",
    "name": "obtenir_blocages_par_description",
    "description": (
        "Retourne le nombre de blocages par description, "
        "classés du plus fréquent au moins fréquent."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
},

"obtenir_duree_blocages": {
    "type": "function",
    "name": "obtenir_duree_blocages",
    "description": (
        "Retourne la durée de chaque blocage en secondes."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
},

"obtenir_temps_total_blocage": {
    "type": "function",
    "name": "obtenir_temps_total_blocage",
    "description": (
        "Retourne le temps total de blocage en secondes."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
},

"obtenir_temps_blocage_par_cellule": {
    "type": "function",
    "name": "obtenir_temps_blocage_par_cellule",
    "description": (
        "Retourne le nombre de blocages et le temps total "
        "de blocage pour chaque cellule."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    },
},
# ========================================================
#CELLULES
# ========================================================

    "rechercher_cellule": {
        "type": "function",
        "name": "rechercher_cellule",
        "description": "Recherche les informations d'une cellule à partir de son identifiant.",
        "parameters": {
            "type": "object",
            "properties": {
                "cellule_id": {
                    "type": "integer",
                    "description": "Identifiant de la cellule."
                }
            },
            "required": ["cellule_id"]
        }
    },

    "rechercher_cellules_par_libelle": {
        "type": "function",
        "name": "rechercher_cellules_par_libelle",
        "description": "Recherche les cellules correspondant à un libellé.",
        "parameters": {
            "type": "object",
            "properties": {
                "libelle": {
                    "type": "string",
                    "description": "Libellé de la cellule."
                }
            },
            "required": ["libelle"]
        }
    },

    "rechercher_cellules_par_zone": {
        "type": "function",
        "name": "rechercher_cellules_par_zone",
        "description": "Recherche les cellules appartenant à une zone donnée.",
        "parameters": {
            "type": "object",
            "properties": {
                "zone": {
                    "type": "integer",
                    "description": "Numéro de la zone."
                }
            },
            "required": ["zone"]
        }
    },

    "rechercher_effectif_cellule": {
        "type": "function",
        "name": "rechercher_effectif_cellule",
        "description": "Retourne l'effectif d'une cellule donnée.",
        "parameters": {
            "type": "object",
            "properties": {
                "cellule_id": {
                    "type": "integer",
                    "description": "Identifiant de la cellule."
                }
            },
            "required": ["cellule_id"]
        }
    },

    "rechercher_cellules_par_ressource": {
        "type": "function",
        "name": "rechercher_cellules_par_ressource",
        "description": "Recherche les cellules utilisant une ressource principale donnée.",
        "parameters": {
            "type": "object",
            "properties": {
                "ressource": {
                    "type": "string",
                    "description": "Nom de la ressource principale."
                }
            },
            "required": ["ressource"]
        }
    },




     # ========================================================
    # Conformes
    # ========================================================
"rechercher_conformes_carton": {
    "type": "function",
    "name": "rechercher_conformes_carton",
    "description": "Recherche les pièces conformes associées à un carton.",
    "parameters": {
        "type": "object",
        "properties": {
            "nticket_carton": {
                "type": "integer",
                "description": "Numéro du ticket carton."
            }
        },
        "required": ["nticket_carton"]
    }
},

"rechercher_conformes_reference": {
    "type": "function",
    "name": "rechercher_conformes_reference",
    "description": "Recherche les pièces conformes associées à une référence.",
    "parameters": {
        "type": "object",
        "properties": {
            "reference": {
                "type": "string",
                "description": "Référence du produit."
            }
        },
        "required": ["reference"]
    }
},

"obtenir_conformes_par_reference": {
    "type": "function",
    "name": "obtenir_conformes_par_reference",
    "description": "Retourne le nombre de pièces conformes pour chaque référence.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
},

"obtenir_conformes_par_date": {
    "type": "function",
    "name": "obtenir_conformes_par_date",
    "description": "Retourne le nombre de scans conformes pour une date donnée.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date au format YYYY-MM-DD."
            }
        },
        "required": ["date"]
    }
},

"obtenir_conformes_reference": {
    "type": "function",
    "name": "obtenir_conformes_reference",
    "description": "Retourne le nombre de scans conformes pour une référence donnée.",
    "parameters": {
        "type": "object",
        "properties": {
            "reference": {
                "type": "string",
                "description": "Référence du produit."
            }
        },
        "required": ["reference"]
    }
},


    # ========================================================
    # CARTON
    # ========================================================

    "rechercher_cartons_cellule": {
    "type": "function",
    "name": "rechercher_cartons_cellule",
    "description": "Recherche les cartons associés à une cellule.",
    "parameters": {
        "type": "object",
        "properties": {
            "cellule_id": {
                "type": "integer",
                "description": "Identifiant de la cellule."
            }
        },
        "required": ["cellule_id"]
    }
},

"rechercher_carton_numero": {
    "type": "function",
    "name": "rechercher_carton_numero",
    "description": "Recherche un carton à partir de son numéro de ticket.",
    "parameters": {
        "type": "object",
        "properties": {
            "nticket_carton": {
                "type": "integer",
                "description": "Numéro du ticket carton."
            }
        },
        "required": ["nticket_carton"]
    }
},

"obtenir_quantite_totale_cellule": {
    "type": "function",
    "name": "obtenir_quantite_totale_cellule",
    "description": "Retourne la quantité totale produite dans une cellule.",
    "parameters": {
        "type": "object",
        "properties": {
            "cellule_id": {
                "type": "integer",
                "description": "Identifiant de la cellule."
            }
        },
        "required": ["cellule_id"]
    }
},

"obtenir_cartons_complets": {
    "type": "function",
    "name": "obtenir_cartons_complets",
    "description": "Retourne les cartons ayant l'état complet.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
},


"obtenir_cartons_par_etat": {
    "type": "function",
    "name": "obtenir_cartons_par_etat",
    "description": "Retourne le nombre de cartons pour chaque état.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
},

"obtenir_quantite_par_reference_et_cellule": {
    "type": "function",
    "name": "obtenir_quantite_par_reference_et_cellule",
    "description": "Retourne la quantité totale et le nombre de cartons pour chaque référence et chaque cellule.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
},

"obtenir_production_par_jour": {
    "type": "function",
    "name": "obtenir_production_par_jour",
    "description": "Retourne la production quotidienne avec la quantité totale et le nombre de cartons.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
},

"obtenir_quantite_par_date": {
    "type": "function",
    "name": "obtenir_quantite_par_date",
    "description": "Retourne la quantité totale et le nombre de cartons pour une date donnée.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date au format YYYY-MM-DD."
            }
        },
        "required": ["date"]
    }
},


# ========================================================
# AFFECTATIONS
# ========================================================


"rechercher_piece_annulee_codebarre": {
    "type": "function",
    "name": "rechercher_piece_annulee_codebarre",
    "description": "Recherche une pièce annulée à partir de son code-barres.",
    "parameters": {
        "type": "object",
        "properties": {
            "codebarre": {
                "type": "string",
                "description": "Code-barres de la pièce."
            }
        },
        "required": ["codebarre"]
    }
},

"rechercher_pieces_annulees_carton": {
    "type": "function",
    "name": "rechercher_pieces_annulees_carton",
    "description": "Recherche les pièces annulées associées à un carton.",
    "parameters": {
        "type": "object",
        "properties": {
            "nticket_carton": {
                "type": "integer",
                "description": "Numéro du ticket carton."
            }
        },
        "required": ["nticket_carton"]
    }
},

"obtenir_annulations_par_reference": {
    "type": "function",
    "name": "obtenir_annulations_par_reference",
    "description": "Retourne le nombre d'annulations par référence.",
    "parameters": {
        "type": "object",
        "properties": {}
    }
},

"obtenir_annulations_par_date": {
    "type": "function",
    "name": "obtenir_annulations_par_date",
    "description": "Retourne les annulations pour une date donnée.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date au format YYYY-MM-DD."
            }
        },
        "required": ["date"]
    }
},

"obtenir_resume_annulations_cellule": {
    "type": "function",
    "name": "obtenir_resume_annulations_cellule",
    "description": "Retourne le résumé des annulations pour une cellule.",
    "parameters": {
        "type": "object",
        "properties": {
            "cellule_id": {
                "type": "integer",
                "description": "Identifiant de la cellule."
            }
        },
        "required": ["cellule_id"]
    }
},


 # ========================================================
    # POINTAGE
    # ========================================================

"rechercher_pointage_employe": {
    "type": "function",
    "name": "rechercher_pointage_employe",
    "description": "Recherche le pointage d'un employé à partir de son matricule.",
    "parameters": {
        "type": "object",
        "properties": {
            "matricule": {
                "type": "integer",
                "description": "Matricule de l'employé."
            }
        },
        "required": ["matricule"]
    }
},

"rechercher_pointage_employe_date": {
    "type": "function",
    "name": "rechercher_pointage_employe_date",
    "description": "Recherche le pointage d'un employé pour une date donnée.",
    "parameters": {
        "type": "object",
        "properties": {
            "matricule": {
                "type": "integer",
                "description": "Matricule de l'employé."
            },
            "date": {
                "type": "string",
                "description": "Date du pointage au format YYYY-MM-DD."
            }
        },
        "required": ["matricule", "date"]
    }
},


"compter_employes_cellule_date": {
    "type": "function",
    "name": "compter_employes_cellule_date",
    "description": "Compte le nombre d'employés ayant pointé dans une cellule à une date donnée.",
    "parameters": {
        "type": "object",
        "properties": {
            "cellule_id": {
                "type": "integer",
                "description": "Identifiant de la cellule."
            },
            "date": {
                "type": "string",
                "description": "Date du pointage au format YYYY-MM-DD."
            }
        },
        "required": ["cellule_id", "date"]
    }
},


"compter_employes_par_cellule": {
    "type": "function",
    "name": "compter_employes_par_cellule",
    "description": "Donne le nombre d'employés ayant pointé dans chaque cellule pour une date donnée.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date du pointage au format YYYY-MM-DD."
            }
        },
        "required": ["date"]
    }
},


# ========================================================
# REWORK
# ========================================================

"rechercher_rework_codebarre": {
    "type": "function",
    "name": "rechercher_rework_codebarre",
    "description": (
        "Recherche les reworks associés à un code-barres."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "codebarre": {
                "type": "string",
                "description": "Code-barres de la pièce."
            }
        },
        "required": ["codebarre"]
    }
},

"rechercher_reworks_reference": {
    "type": "function",
    "name": "rechercher_reworks_reference",
    "description": (
        "Recherche les reworks associés à une référence."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "reference": {
                "type": "string",
                "description": "Référence de la pièce."
            }
        },
        "required": ["reference"]
    }
},

"obtenir_reworks_par_defaut": {
    "type": "function",
    "name": "obtenir_reworks_par_defaut",
    "description": (
        "Retourne le nombre de reworks par défaut, "
        "classés du plus fréquent au moins fréquent."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
},

"rechercher_reworks_operateur": {
    "type": "function",
    "name": "rechercher_reworks_operateur",
    "description": (
        "Recherche les reworks associés à un opérateur "
        "à partir de son matricule."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "matricule": {
                "type": "integer",
                "description": "Matricule de l'opérateur."
            }
        },
        "required": ["matricule"]
    }
},

"obtenir_reworks_par_date": {
    "type": "function",
    "name": "obtenir_reworks_par_date",
    "description": (
        "Retourne le nombre de reworks pour une date donnée."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date au format YYYY-MM-DD."
            }
        },
        "required": ["date"]
    }
},

 # ========================================================
    # SCRAP
    # ========================================================

"rechercher_scrap_codebarre": {
    "type": "function",
    "name": "rechercher_scrap_codebarre",
    "description": (
        "Recherche les scraps associés à un code-barres."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "codebarre": {
                "type": "string",
                "description": "Code-barres de la pièce."
            }
        },
        "required": ["codebarre"]
    }
},

"rechercher_scraps_reference": {
    "type": "function",
    "name": "rechercher_scraps_reference",
    "description": (
        "Recherche les scraps associés à une référence."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "reference": {
                "type": "string",
                "description": "Référence de la pièce."
            }
        },
        "required": ["reference"]
    }
},

"rechercher_scraps_cellule": {
    "type": "function",
    "name": "rechercher_scraps_cellule",
    "description": (
        "Recherche les scraps associés à une cellule."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "cellule_id": {
                "type": "integer",
                "description": "Identifiant de la cellule."
            }
        },
        "required": ["cellule_id"]
    }
},

"obtenir_scraps_par_defaut": {
    "type": "function",
    "name": "obtenir_scraps_par_defaut",
    "description": (
        "Retourne le nombre de scraps par défaut, "
        "classés du plus fréquent au moins fréquent."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
},

"obtenir_scraps_par_operateur": {
    "type": "function",
    "name": "obtenir_scraps_par_operateur",
    "description": (
        "Retourne le nombre de scraps par opérateur, "
        "classés du plus fréquent au moins fréquent."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
},

"rechercher_scraps_operateur": {
    "type": "function",
    "name": "rechercher_scraps_operateur",
    "description": (
        "Recherche les scraps associés à un opérateur "
        "à partir de son matricule."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "matricule": {
                "type": "integer",
                "description": "Matricule de l'opérateur."
            }
        },
        "required": ["matricule"]
    }
},

"obtenir_scraps_par_date": {
    "type": "function",
    "name": "obtenir_scraps_par_date",
    "description": (
        "Retourne le nombre de scraps pour une date donnée."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date au format YYYY-MM-DD."
            }
        },
        "required": ["date"]
    }
},

"obtenir_scraps_par_reference_et_defaut": {
    "type": "function",
    "name": "obtenir_scraps_par_reference_et_defaut",
    "description": (
        "Retourne le nombre de scraps par référence et par défaut, "
        "classés du plus fréquent au moins fréquent."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
},





    # ========================================================
    # RAG
    # ========================================================
        

"rechercher_documents": {
    "type": "function",
    "name": "rechercher_documents",
    "description": (
        "Recherche dans les documents de l'entreprise "
        "les informations pertinentes pour répondre à une question. "
        "Utilise ce tool pour les procédures, instructions, guides, "
        "manuels et informations présentes dans les documents."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": (
                    "Question ou recherche à effectuer "
                    "dans les documents."
                ),
            },
            "top_k": {
                "type": "integer",
                "description": (
                    "Nombre de passages pertinents à récupérer. "
                    "Utiliser 5 par défaut."
                ),
            },
        },
        "required": ["question"],
    },
},
    # ========================================================
    # AFFECTATIONS
    # ========================================================

    

    "rechercher_affectations_cellule": {
        "type": "function",
        "name": "rechercher_affectations_cellule",
        "description": (
            "Recherche les affectations associées à une cellule."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "cellule_id": {
                    "type": "integer",
                    "description": "Identifiant de la cellule.",
                }
            },
            "required": ["cellule_id"],
        },
    },

    "rechercher_affectation_matricule": {
        "type": "function",
        "name": "rechercher_affectation_matricule",
        "description": (
            "Recherche l'affectation d'un employé."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "matricule": {
                    "type": "integer",
                    "description": "Matricule de l'employé.",
                }
            },
            "required": ["matricule"],
        },
    },

    "rechercher_personnes_bloc": {
        "type": "function",
        "name": "rechercher_personnes_bloc",
        "description": (
            "Recherche les personnes affectées à un bloc."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "bloc": {
                    "type": "string",
                    "description": "Nom ou identifiant du bloc.",
                }
            },
            "required": ["bloc"],
        },
    },

    "obtenir_employes_par_bloc": {
        "type": "function",
        "name": "obtenir_employes_par_bloc",
        "description": (
            "Retourne le nombre d'employés distincts par bloc."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    "obtenir_employes_par_cellule": {
        "type": "function",
        "name": "obtenir_employes_par_cellule",
        "description": (
            "Retourne le nombre d'employés distincts par cellule."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    "obtenir_employes_par_emplacement": {
        "type": "function",
        "name": "obtenir_employes_par_emplacement",
        "description": (
            "Retourne le nombre d'employés distincts "
            "par emplacement, cellule et bloc."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
}


# ============================================================
# 3. CONSTRUIRE LES TOOLS GEMINI A PARTIR DES DOMAINES
# ============================================================

def get_gemini_tools_for_domains(domains: list[str]):

    selected_tools = []

    # domain_tools.py nous donne les tools autorisés
    domain_tools = get_tools_for_domains(domains)

    for tool_name in domain_tools:

        if tool_name in GEMINI_TOOL_DEFINITIONS:
            selected_tools.append(
                GEMINI_TOOL_DEFINITIONS[tool_name]
            )

    return selected_tools


# ============================================================
# 4. EXECUTION D'UN TOOL
# ============================================================

def execute_tool(tool_name: str, arguments: dict):

    if tool_name not in TOOLS:
        raise ValueError(
            f"Tool inconnu : {tool_name}"
        )

    tool_function = TOOLS[tool_name]

    return tool_function(**arguments)


# ============================================================
# 5. AGENT PRINCIPAL
# ============================================================

def ask_agent(question: str, session_id: str):

    # ========================================================
    # MEMOIRE CONVERSATIONNELLE
    # ========================================================

    if session_id not in conversation_memory:
        conversation_memory[session_id] = {
        "interaction_id": None,
        "history": []
    }

    memory = conversation_memory[session_id]

    previous_interaction_id = memory["interaction_id"]

    # ========================================================
    # 1. DETECTER LE DOMAIN
    # ========================================================

    conversation_context = ""

    if memory["history"]:
        conversation_context = "\n".join(
        f"{message['role']}: {message['content']}"
        for message in memory["history"]
    )
    domains = detect_domains(question , conversation_context)

    print("\n==============================")
    print("QUESTION")
    print("==============================")
    print(question)

    print("\n==============================")
    print("DOMAINES DETECTES")
    print("==============================")
    print(domains)

    # Aucun domaine détecté
    if not domains:
        return (
            "Je n'ai pas identifié le domaine de données "
            "nécessaire pour répondre à cette question."
        )

    # ========================================================
    # 2. RECUPERER LES TOOLS DU DOMAIN
    # ========================================================

    gemini_tools = get_gemini_tools_for_domains(domains)

    print("\n==============================")
    print("TOOLS ACTIVES")
    print("==============================")

    for tool in gemini_tools:
        print("-", tool["name"])

    # ========================================================
    # 3. APPEL INITIAL GEMINI
    # ========================================================

    AGENT_INSTRUCTIONS = """
Tu es un assistant intelligent pour interroger les données industrielles.

Règles importantes :

1. N'appelle jamais un outil si un paramètre obligatoire est manquant.

2. Par défaut, lorsqu'un utilisateur demande simplement "l'efficience"
   sans préciser opérateur ou shift, interprète la demande comme une
   demande concernant l'efficience d'une cellule.

3. Pour rechercher l'efficience d'une cellule avec le tool
   rechercher_efficience_cellule, la cellule ET la date sont obligatoires.

4. Si la cellule ou la date manque, demande uniquement l'information manquante.

Exemple :
Utilisateur : "Quelle est l'efficience ?"
Assistant : "De quelle cellule et de quelle date parlez-vous ?"

Exemple :
Utilisateur : "Quelle est l'efficience de la cellule 19 ?"
Assistant : "Pour quelle date voulez-vous connaître l'efficience de la cellule 19 ?"

Exemple :
Utilisateur : "Quelle est l'efficience le 17/04/2023 ?"
Assistant : "De quelle cellule parlez-vous ?"

Exemple :
Utilisateur : "Quelle est l'efficience de la cellule 19 le 17/04/2023 ?"
Assistant : utiliser le tool rechercher_efficience_cellule.

5. Ne devine jamais une cellule ou une date.

6. Si les informations nécessaires sont absentes, pose une question de clarification
   au lieu d'appeler un outil avec des valeurs inventées.

7. Si l'utilisateur précise explicitement un opérateur ou un shift,
   utilise le tool correspondant.

8. Pour les questions concernant des procédures, instructions,
   guides, manuels ou documents de l'entreprise, utilise le tool
   rechercher_documents.

9. Lorsque le tool RAG retourne des documents, utilise leur contenu
   pour construire la réponse.

10. Ne prétends jamais qu'une information vient des documents
    si elle n'est pas présente dans les résultats retournés.

11. Réponds en français ou arabe ou anglais ca depend au question.

"""


    interaction_args = {
    "model": "gemini-3.6-flash",
    "input": question,
    "tools": gemini_tools,
    "generation_config": {
        "thinking_level": "low"
    },
    "system_instruction": AGENT_INSTRUCTIONS
}

    if previous_interaction_id:
        interaction_args["previous_interaction_id"] = previous_interaction_id

    response = client.interactions.create(**interaction_args)


    # ========================================================
    # 4. RECUPERER LES FUNCTION CALLS
    # ========================================================

    function_calls = []

    # IMPORTANT :
    # Interactions API utilise maintenant "steps"
    # et non plus "outputs".

    for step in response.steps:

        if step.type == "function_call":

            function_calls.append(step)

    # ========================================================
    # 5. SI AUCUN TOOL N'EST APPELE
    # ========================================================

    if not function_calls:

        conversation_memory[session_id]["interaction_id"] = response.id

        conversation_memory[session_id]["history"].append({
        "role": "user",
        "content": question
        })

        conversation_memory[session_id]["history"].append({
        "role": "assistant",
        "content": response.output_text
        })
        return response.output_text

    # ========================================================
    # 6. EXECUTER LES TOOLS
    # ========================================================

    function_results = []

    for call in function_calls:

        tool_name = call.name
        arguments = call.arguments

        print("\n==============================")
        print("TOOL APPELE")
        print("==============================")

        print("Tool :", tool_name)
        print("Arguments :", arguments)

        try:

            result = execute_tool(
                tool_name,
                arguments
            )

            print("\nRESULTAT :")
            print(result)

            function_results.append({
                "type": "function_result",
                "name": tool_name,
                "call_id": call.id,
                "result": [
                    {
                        "type": "text",
                        "text": str(result)
                    }
                ],
            })

        except Exception as e:

            print("\nERREUR TOOL :")
            print(str(e))

            function_results.append({
                "type": "function_result",
                "name": tool_name,
                "call_id": call.id,
                "result": [
                    {
                        "type": "text",
                        "text": f"Erreur lors de l'exécution du tool : {str(e)}"
                    }
                ],
            })

    # ========================================================
    # 7. RENVOYER LES RESULTATS A GEMINI
    # ========================================================

    final_response = client.interactions.create(

        model="gemini-3.6-flash",

        previous_interaction_id=response.id,

        input=function_results,

        tools=gemini_tools,

        generation_config={
            "thinking_level": "low"
        },
    )

    # ========================================================
    # 8. REPONSE FINALE
    # ========================================================

    conversation_memory[session_id]["interaction_id"] = final_response.id

    conversation_memory[session_id]["history"].append({
    "role": "user",
    "content": question
    })

    conversation_memory[session_id]["history"].append({
    "role": "assistant",
    "content": final_response.output_text
    })

    return final_response.output_text