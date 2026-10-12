
from sqlalchemy import text

from app.db.database import engine
from app.cache.redis_cache import get_cache, set_cache


CACHE_TTL = 300  # 5 minutes


def get_efficience_cellule(cellule_id: int, date: str):
    cache_key = f"efficience:cellule:{cellule_id}:date:{date}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            date,
            zone,
            cellule_id,
            shift_id,
            matricule,
            fonction,
            time_shift,
            curr_time_shift,
            efficience,
            ppm,
            etat
        FROM efficience_cellule
        WHERE cellule_id = :cellule_id
          AND date = :date
        ORDER BY date DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "cellule_id": cellule_id,
                "date": date
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


def get_efficience_operateur(matricule: int):
    cache_key = f"efficience:operateur:{matricule}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            date,
            zone,
            cellule_id,
            shift_id,
            matricule,
            fonction,
            time_shift,
            curr_time_shift,
            efficience,
            ppm,
            etat
        FROM efficience_cellule
        WHERE matricule = :matricule
        ORDER BY date DESC
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "matricule": matricule
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


def get_efficience_cellules_date(date: str):
    """
    Retourne l'efficience de toutes les cellules
    pour une date donnée.
    """

    cache_key = f"efficience:cellules:date:{date}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cellule_id,
            date,
            zone,
            shift_id,
            matricule,
            fonction,
            time_shift,
            curr_time_shift,
            efficience,
            ppm,
            etat
        FROM efficience_cellule
        WHERE date = :date
        ORDER BY cellule_id
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "date": date
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


def get_efficience_by_shift(shift_id: int, date: str):
    cache_key = f"efficience:shift:{shift_id}:date:{date}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            date,
            zone,
            cellule_id,
            shift_id,
            matricule,
            fonction,
            efficience,
            ppm
        FROM efficience_cellule
        WHERE shift_id = :shift_id
          AND date = :date
        ORDER BY cellule_id, matricule
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "shift_id": shift_id,
                "date": date
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
