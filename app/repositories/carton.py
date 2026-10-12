
from sqlalchemy import text

from app.db.database import engine
from app.cache.redis_cache import get_cache, set_cache


CACHE_TTL = 300  # 5 minutes


def get_cartons_by_cellule(cellule_id: int):
    cache_key = f"carton:cellule:{cellule_id}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            nticket_carton,
            qte_carton,
            reference,
            code_fournisseur,
            date,
            date_cloture,
            etat,
            cellule_id,
            etat_audit
        FROM carton
        WHERE cellule_id = :cellule_id
        ORDER BY date DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"cellule_id": cellule_id}
        )

        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_carton_by_number(nticket_carton: int):
    cache_key = f"carton:number:{nticket_carton}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            nticket_carton,
            qte_carton,
            reference,
            code_fournisseur,
            date,
            date_cloture,
            etat,
            cellule_id,
            etat_audit
        FROM carton
        WHERE nticket_carton = :nticket_carton;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"nticket_carton": nticket_carton}
        )

        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_total_quantity_by_cellule(cellule_id: int):
    cache_key = f"carton:quantity:cellule:{cellule_id}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cellule_id,
            SUM(qte_carton) AS quantite_totale
        FROM carton
        WHERE cellule_id = :cellule_id
        GROUP BY cellule_id;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"cellule_id": cellule_id}
        )

        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_complete_cartons():
    cache_key = "carton:complete"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            nticket_carton,
            qte_carton,
            reference,
            date,
            date_cloture,
            cellule_id
        FROM carton
        WHERE etat = 'complet'
        ORDER BY date DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_cartons_by_state():
    cache_key = "carton:by_state"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            etat,
            COUNT(DISTINCT nticket_carton) AS nombre_cartons
        FROM carton
        GROUP BY etat
        ORDER BY nombre_cartons DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_quantity_by_reference_and_cellule():
    cache_key = "carton:quantity:reference_cellule"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            reference,
            cellule_id,
            SUM(qte_carton) AS quantite_totale,
            COUNT(DISTINCT nticket_carton) AS nombre_cartons
        FROM carton
        GROUP BY
            reference,
            cellule_id
        ORDER BY
            reference,
            cellule_id;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_production_by_day():
    cache_key = "carton:production_by_day"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            DATE(date) AS jour,
            SUM(qte_carton) AS quantite_totale,
            COUNT(DISTINCT nticket_carton) AS nombre_cartons
        FROM carton
        GROUP BY DATE(date)
        ORDER BY jour DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_quantity_by_date(date: str):
    cache_key = f"carton:quantity:date:{date}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            SUM(qte_carton) AS quantite_totale,
            COUNT(DISTINCT nticket_carton) AS nombre_cartons
        FROM carton
        WHERE DATE(date) = :date;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"date": date}
        )

        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data
