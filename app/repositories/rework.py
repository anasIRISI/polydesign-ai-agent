from sqlalchemy import text
from app.db.database import engine


def get_rework_by_codebarre(codebarre: str):
    query = text("""
        SELECT
            id,
            codebarre,
            code AS reference,
            defaut,
            matricule,
            date,
            heure,
            cellule_id,
            shift_id,
            controlleur,
            poste,
            cause
        FROM rework
        WHERE codebarre = :codebarre
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"codebarre": codebarre}
        )

        return [dict(row._mapping) for row in result]


def get_reworks_by_reference(reference: str):
    query = text("""
        SELECT
            id,
            codebarre,
            code AS reference,
            defaut,
            matricule,
            date,
            heure,
            cellule_id,
            shift_id,
            controlleur,
            poste,
            cause
        FROM rework
        WHERE code = :reference
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"reference": reference}
        )

        return [dict(row._mapping) for row in result]


def get_reworks_by_defaut():
    query = text("""
        SELECT
            defaut,
            COUNT(*) AS nombre_reworks
        FROM rework
        GROUP BY defaut
        ORDER BY nombre_reworks DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row._mapping) for row in result]


def get_reworks_by_matricule(matricule: int):
    query = text("""
        SELECT
            matricule,
            code AS reference,
            codebarre,
            defaut,
            date,
            heure,
            cellule_id,
            shift_id,
            controlleur,
            poste,
            cause
        FROM rework
        WHERE matricule = :matricule
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"matricule": matricule}
        )

        return [dict(row._mapping) for row in result]


def get_reworks_by_date(date):
    query = text("""
        SELECT
            date,
            COUNT(*) AS nombre_reworks
        FROM rework
        WHERE date = :date
        GROUP BY date;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"date": date}
        )

        return [dict(row._mapping) for row in result]