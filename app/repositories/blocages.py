
from sqlalchemy import text

from app.db.database import engine
from app.cache.redis_cache import get_cache, set_cache


CACHE_TTL = 300  # 5 minutes


def get_blocages_by_cellule(cellule_id: int):
    cache_key = f"blocages:cellule:{cellule_id}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            cellule_id,
            shift_id,
            date,
            description,
            cause,
            heure_debut,
            heure_fin,
            unblocked_by,
            allowed_responsable,
            controlleur,
            poste
        FROM blocages
        WHERE cellule_id = :cellule_id
        ORDER BY heure_debut DESC;
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


def get_blocages_by_shift(shift_id: int):
    cache_key = f"blocages:shift:{shift_id}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            cellule_id,
            shift_id,
            date,
            description,
            cause,
            heure_debut,
            heure_fin,
            unblocked_by,
            poste
        FROM blocages
        WHERE shift_id = :shift_id
        ORDER BY heure_debut DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"shift_id": shift_id}
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


def get_blocages_by_date(date: str):
    cache_key = f"blocages:date:{date}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            cellule_id,
            shift_id,
            date,
            description,
            cause,
            heure_debut,
            heure_fin,
            unblocked_by,
            poste
        FROM blocages
        WHERE date = :date
        ORDER BY heure_debut;
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


def get_blocages_between_dates(date_debut: str, date_fin: str):
    cache_key = f"blocages:between:{date_debut}:{date_fin}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            cellule_id,
            shift_id,
            date,
            description,
            cause,
            heure_debut,
            heure_fin,
            unblocked_by,
            poste
        FROM blocages
        WHERE date BETWEEN :date_debut AND :date_fin
        ORDER BY date DESC, heure_debut DESC;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "date_debut": date_debut,
                "date_fin": date_fin
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


def get_blocages_by_cellule_count():
    cache_key = "blocages:by_cellule_count"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cellule_id,
            COUNT(*) AS nombre_blocages
        FROM blocages
        GROUP BY cellule_id
        ORDER BY nombre_blocages DESC;
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


def get_blocages_by_cause():
    cache_key = "blocages:by_cause"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cause,
            COUNT(*) AS nombre_blocages
        FROM blocages
        GROUP BY cause
        ORDER BY nombre_blocages DESC;
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


def get_blocages_by_description():
    cache_key = "blocages:by_description"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            description,
            COUNT(*) AS nombre_blocages
        FROM blocages
        GROUP BY description
        ORDER BY nombre_blocages DESC;
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


def get_blocages_duration():
    cache_key = "blocages:duration"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            id,
            cellule_id,
            shift_id,
            date,
            description,
            cause,
            heure_debut,
            heure_fin,
            TIMESTAMPDIFF(
                SECOND,
                heure_debut,
                heure_fin
            ) AS duree_secondes
        FROM blocages
        ORDER BY heure_debut DESC;
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


def get_total_blocage_time():
    cache_key = "blocages:total_time"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            SUM(
                TIMESTAMPDIFF(
                    SECOND,
                    heure_debut,
                    heure_fin
                )
            ) AS temps_total_blocage_secondes
        FROM blocages
        WHERE heure_debut IS NOT NULL
          AND heure_fin IS NOT NULL;
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


def get_total_blocage_time_by_cellule():
    cache_key = "blocages:total_time_by_cellule"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cellule_id,
            COUNT(*) AS nombre_blocages,
            SUM(
                TIMESTAMPDIFF(
                    SECOND,
                    heure_debut,
                    heure_fin
                )
            ) AS temps_total_blocage_secondes
        FROM blocages
        WHERE heure_debut IS NOT NULL
          AND heure_fin IS NOT NULL
        GROUP BY cellule_id
        ORDER BY temps_total_blocage_secondes DESC;
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
