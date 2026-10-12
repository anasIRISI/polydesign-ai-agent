from sqlalchemy import text
from app.db.database import engine


def get_pointage_by_matricule(matricule: int):
    query = text("""
        SELECT
            id,
            matricule,
            date,
            heure_entree,
            heure_sortie,
            cellule_id,
            shift_id,
            poste,
            operation,
            etat,
            machine
        FROM pointage
        WHERE matricule = :matricule
        ORDER BY date DESC, heure_entree DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"matricule": matricule}
        )

        return [dict(row._mapping) for row in result]


def get_pointage_by_matricule_and_date(matricule: int, date):
    query = text("""
        SELECT
            matricule,
            date,
            heure_entree,
            heure_sortie,
            cellule_id,
            shift_id,
            poste,
            operation,
            etat,
            machine
        FROM pointage
        WHERE matricule = :matricule
          AND date = :date;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "matricule": matricule,
                "date": date
            }
        )

        return [dict(row._mapping) for row in result]


def get_employes_by_cellule_and_date(cellule_id: int, date):
    query = text("""
        SELECT
            cellule_id,
            COUNT(DISTINCT matricule) AS nombre_employes
        FROM pointage
        WHERE cellule_id = :cellule_id
          AND date = :date
        GROUP BY cellule_id;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "cellule_id": cellule_id,
                "date": date
            }
        )

        return [dict(row._mapping) for row in result]


def get_employes_by_cellule(date):
    query = text("""
        SELECT
            cellule_id,
            COUNT(DISTINCT matricule) AS nombre_employes
        FROM pointage
        WHERE date = :date
        GROUP BY cellule_id
        ORDER BY nombre_employes DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"date": date}
        )

        return [dict(row._mapping) for row in result]