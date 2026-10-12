from sqlalchemy import text

from app.db.database import engine
from app.cache.redis_cache import get_cache, set_cache


CACHE_TTL = 300  # 5 minutes


def get_cellule_by_id(cellule_id: int):
    cache_key = f"cellule:id:{cellule_id}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. Si absent du cache → MySQL
    query = text("""
        SELECT
            id,
            libelle,
            zone,
            effectif,
            prime,
            calendrier,
            ressource_principal,
            percentage_tolerance,
            date_creation,
            date_modification
        FROM cellules
        WHERE id = :cellule_id
          AND delet = 0
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "cellule_id": cellule_id
            }
        )

        row = result.fetchone()

    if row is None:
        return None

    data = dict(row._mapping)

    # 3. Stocker le résultat dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def search_cellules_by_libelle(libelle: str):
    cache_key = f"cellule:libelle:{libelle.strip().lower()}"

    # 1. Cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            libelle,
            zone,
            effectif,
            prime,
            calendrier,
            ressource_principal
        FROM cellules
        WHERE libelle LIKE CONCAT('%', :libelle, '%')
          AND delet = 0
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "libelle": libelle
            }
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


def get_cellules_by_zone(zone: int):
    cache_key = f"cellule:zone:{zone}"

    # 1. Cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            libelle,
            zone,
            effectif,
            ressource_principal
        FROM cellules
        WHERE zone = :zone
          AND delet = 0
        ORDER BY id
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "zone": zone
            }
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


def get_cellule_effectif(cellule_id: int):
    cache_key = f"cellule:effectif:{cellule_id}"

    # 1. Cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            libelle,
            effectif
        FROM cellules
        WHERE id = :cellule_id
          AND delet = 0
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "cellule_id": cellule_id
            }
        )

        row = result.fetchone()

    if row is None:
        return None

    data = dict(row._mapping)

    # 3. Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_cellules_by_ressource(ressource: str):
    cache_key = f"cellule:ressource:{ressource.strip().lower()}"

    # 1. Cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            libelle,
            zone,
            effectif,
            ressource_principal
        FROM cellules
        WHERE ressource_principal = :ressource
          AND delet = 0
        ORDER BY id
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "ressource": ressource
            }
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