from sqlalchemy import text
from app.db.database import engine


def get_piece_annulee_by_codebarre(codebarre: str):
    query = text("""
        SELECT
            id,
            codebarre,
            code AS reference,
            nticket_carton,
            date_declaration,
            date_annulation,
            cellule_id,
            shift_id,
            controlleur,
            etat
        FROM pieces_annulee
        WHERE codebarre = :codebarre;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"codebarre": codebarre}
        )

        return [dict(row._mapping) for row in result.fetchall()]


def get_pieces_annulees_by_carton(nticket_carton: int):
    query = text("""
        SELECT
            id,
            codebarre,
            code AS reference,
            nticket_carton,
            date_declaration,
            date_annulation,
            cellule_id,
            shift_id,
            controlleur,
            etat
        FROM pieces_annulee
        WHERE nticket_carton = :nticket_carton
        ORDER BY date_annulation DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"nticket_carton": nticket_carton}
        )

        return [dict(row._mapping) for row in result.fetchall()]


def get_annulations_by_reference():
    query = text("""
        SELECT
            code AS reference,
            COUNT(*) AS nombre_annulations
        FROM pieces_annulee
        GROUP BY code
        ORDER BY nombre_annulations DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row._mapping) for row in result.fetchall()]


def get_annulations_by_date(date):
    query = text("""
        SELECT
            DATE(date_annulation) AS jour,
            COUNT(*) AS nombre_annulations
        FROM pieces_annulee
        WHERE DATE(date_annulation) = :date
        GROUP BY DATE(date_annulation);
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"date": date}
        )

        return [dict(row._mapping) for row in result.fetchall()]


def get_annulation_summary_by_cellule(cellule_id: int):
    query = text("""
        SELECT
            cellule_id,
            COUNT(*) AS total_annulations,
            COUNT(DISTINCT code) AS references_concernees,
            COUNT(DISTINCT nticket_carton) AS cartons_concernes,
            COUNT(DISTINCT controlleur) AS controleurs
        FROM pieces_annulee
        WHERE cellule_id = :cellule_id
        GROUP BY cellule_id;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"cellule_id": cellule_id}
        )

        return [dict(row._mapping) for row in result.fetchall()]