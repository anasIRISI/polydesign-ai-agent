
from sqlalchemy import text

from app.db.database import engine
from app.cache.redis_cache import get_cache, set_cache


CACHE_TTL = 300  # 5 minutes


def get_affectations_by_cellule(cellule_id: int):
    cache_key = f"affectations:cellule:{cellule_id}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            port_id,
            cellule_id,
            bloc,
            emplacement,
            matricule
        FROM affectations
        WHERE cellule_id = :cellule_id
        ORDER BY bloc, emplacement;
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

    # 3. Stocker dans Redis
    set_cache(
        cache_key,
        data,
        ttl=CACHE_TTL
    )

    return data


def get_affectation_by_matricule(matricule: int):
    cache_key = f"affectations:matricule:{matricule}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            port_id,
            cellule_id,
            bloc,
            emplacement,
            matricule
        FROM affectations
        WHERE matricule = :matricule;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"matricule": matricule}
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


def get_personnes_by_bloc(bloc: str):
    cache_key = f"affectations:bloc:{bloc.strip().lower()}"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            matricule,
            port_id,
            cellule_id,
            emplacement
        FROM affectations
        WHERE bloc = :bloc
        ORDER BY emplacement, matricule;
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"bloc": bloc}
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


def get_employes_by_bloc():
    cache_key = "affectations:employes_by_bloc"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            bloc,
            COUNT(DISTINCT matricule) AS nombre_employes
        FROM affectations
        GROUP BY bloc
        ORDER BY nombre_employes DESC;
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


def get_employes_by_cellule():
    cache_key = "affectations:employes_by_cellule"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cellule_id,
            COUNT(DISTINCT matricule) AS nombre_employes
        FROM affectations
        GROUP BY cellule_id
        ORDER BY cellule_id;
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


def get_employes_by_emplacement():
    cache_key = "affectations:employes_by_emplacement"

    # 1. Vérifier le cache
    cached = get_cache(cache_key)

    if cached is not None:
        return cached

    # 2. MySQL
    query = text("""
        SELECT
            cellule_id,
            bloc,
            emplacement,
            COUNT(DISTINCT matricule) AS nombre_employes
        FROM affectations
        GROUP BY
            cellule_id,
            bloc,
            emplacement
        ORDER BY
            cellule_id,
            bloc,
            emplacement;
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
