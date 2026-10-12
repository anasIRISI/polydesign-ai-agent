
import time

from app.repositories.efficience_cellule import (
    get_efficience_cellule,
    get_efficience_operateur,
    get_efficience_cellules_date,
    get_efficience_by_shift,
)
from app.cache.redis_cache import get_cache


# ============================================================
# PARAMÈTRES DE TEST
# ============================================================

CELLULE_ID = 17
DATE = "2023-04-17"
MATRICULE = 93
SHIFT_ID = 2


# ============================================================
# 1. TEST : EFFICIENCE D'UNE CELLULE À UNE DATE
# ============================================================

print("\n==============================================")
print("1. TEST get_efficience_cellule()")
print("==============================================")

cache_key = f"efficience:cellule:{CELLULE_ID}:date:{DATE}"

print("\n--- PREMIER APPEL ---")

start = time.perf_counter()

result = get_efficience_cellule(
    CELLULE_ID,
    DATE
)

end = time.perf_counter()

print("Résultat :", result)
print(f"Temps : {(end - start) * 1000:.2f} ms")

print("\n--- DEUXIÈME APPEL ---")

start = time.perf_counter()

result = get_efficience_cellule(
    CELLULE_ID,
    DATE
)

end = time.perf_counter()

print("Résultat :", result)
print(f"Temps : {(end - start) * 1000:.2f} ms")

print("\n--- REDIS ---")

print("Clé :", cache_key)
print("Cache :", get_cache(cache_key))
