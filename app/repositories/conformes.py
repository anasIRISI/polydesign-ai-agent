from sqlalchemy import text
from app.db.database import engine


def get_conformes_by_carton(nticket_carton: int):
    query = text("""
        SELECT
            codebarre,
            code,
            nticket_carton,
            date,
            heure,
            cellule_id,
            shift_id,
            controlleur,
            etat,
            poste,
            cause
        FROM conformes
        WHERE nticket_carton = :nticket_carton
        ORDER BY date, heure;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"nticket_carton": nticket_carton}
        )

        return [dict(row._mapping) for row in result.fetchall()]


def get_conformes_by_reference(reference: str):
    query = text("""
        SELECT
            codebarre,
            code,
            nticket_carton,
            date,
            heure,
            cellule_id,
            shift_id,
            controlleur,
            etat,
            poste,
            cause
        FROM conformes
        WHERE code = :reference
        ORDER BY date DESC, heure DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"reference": reference}
        )

        return [dict(row._mapping) for row in result.fetchall()]


def get_all_conformes_count_by_reference():
    query = text("""
        SELECT
            code AS reference,
            COUNT(*) AS nombre_enregistrements
        FROM conformes
        GROUP BY code
        ORDER BY nombre_enregistrements DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row._mapping) for row in result.fetchall()]

def get_conformes_count_by_date(date):
    query = text("""
        SELECT
            date,
            COUNT(*) AS nombre_scans
        FROM conformes
        WHERE date = :date
        GROUP BY date;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"date": date}
        )

        return [dict(row._mapping) for row in result.fetchall()]


def get_conformes_count_by_reference(reference: str):
    query = text("""
        SELECT
            code AS reference,
            COUNT(*) AS nombre_scans
        FROM conformes
        WHERE code = :reference
        GROUP BY code;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"reference": reference}
        )

        return [dict(row._mapping) for row in result.fetchall()]