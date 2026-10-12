from sqlalchemy import text
from app.db.database import engine


def get_scrap_by_codebarre(codebarre: str):
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
        FROM scrap
        WHERE codebarre = :codebarre
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"codebarre": codebarre}
        )

        return [dict(row._mapping) for row in result]


def get_scraps_by_reference(reference: str):
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
        FROM scrap
        WHERE code = :reference
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"reference": reference}
        )

        return [dict(row._mapping) for row in result]


def get_scraps_by_cellule(cellule_id: int):
    query = text("""
        SELECT
            id,
            codebarre,
            code AS reference,
            defaut,
            matricule,
            date,
            heure,
            shift_id,
            controlleur,
            poste,
            cause
        FROM scrap
        WHERE cellule_id = :cellule_id
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"cellule_id": cellule_id}
        )

        return [dict(row._mapping) for row in result]


def get_scraps_by_defaut():
    query = text("""
        SELECT
            defaut,
            COUNT(*) AS nombre_scraps
        FROM scrap
        GROUP BY defaut
        ORDER BY nombre_scraps DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row._mapping) for row in result]


def get_scraps_by_operateur():
    query = text("""
        SELECT
            matricule,
            COUNT(*) AS nombre_scraps
        FROM scrap
        GROUP BY matricule
        ORDER BY nombre_scraps DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row._mapping) for row in result]


def get_scraps_by_matricule(matricule: int):
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
        FROM scrap
        WHERE matricule = :matricule
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"matricule": matricule}
        )

        return [dict(row._mapping) for row in result]


def get_scraps_by_date(date):
    query = text("""
        SELECT
            date,
            COUNT(*) AS nombre_scraps
        FROM scrap
        WHERE date = :date
        GROUP BY date;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"date": date}
        )

        return [dict(row._mapping) for row in result]


def get_scraps_by_reference_and_defaut():
    query = text("""
        SELECT
            code AS reference,
            defaut,
            COUNT(*) AS nombre_scraps
        FROM scrap
        GROUP BY
            code,
            defaut
        ORDER BY nombre_scraps DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row._mapping) for row in result]