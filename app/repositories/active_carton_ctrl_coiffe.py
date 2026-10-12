
from sqlalchemy import text

from app.db.database import engine
from app.cache.redis_cache import get_cache, set_cache


CACHE_TTL = 300  # 5 minutes


def get_cartons_by_reference():
    cache_key = "cartons:by_reference"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            reference,
            COUNT(DISTINCT carton) AS nombre_cartons
        FROM active_carton_ctrl_coiffe
        GROUP BY reference
        ORDER BY nombre_cartons DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Stocker dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_references():
    cache_key = "cartons:references"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT DISTINCT
            reference
        FROM active_carton_ctrl_coiffe
        ORDER BY reference
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Stocker dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_cartons_by_machine(machine: str):
    cache_key = f"cartons:machine:{machine.strip().lower()}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            carton,
            reference,
            cellule_id,
            shift_id,
            poste,
            machine
        FROM active_carton_ctrl_coiffe
        WHERE machine = :machine
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "machine": machine
            }
        )

        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Stocker dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_cartons_by_machine_count():
    cache_key = "cartons:by_machine_count"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            machine,
            COUNT(*) AS nombre_cartons
        FROM active_carton_ctrl_coiffe
        GROUP BY machine
        ORDER BY nombre_cartons DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Stocker dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_cartons_by_cellule():
    cache_key = "cartons:by_cellule"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cellule_id,
            COUNT(DISTINCT carton) AS nombre_cartons
        FROM active_carton_ctrl_coiffe
        GROUP BY cellule_id
        ORDER BY nombre_cartons DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Stocker dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_cartons_by_shift():
    cache_key = "cartons:by_shift"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            shift_id,
            COUNT(DISTINCT carton) AS nombre_cartons
        FROM active_carton_ctrl_coiffe
        GROUP BY shift_id
        ORDER BY shift_id
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    data = [
        dict(row._mapping)
        for row in rows
    ]

    # 3. Stocker dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data
