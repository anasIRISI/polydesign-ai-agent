import time

from app.repositories.cellules import get_cellule_by_id
from app.cache.redis_cache import get_cache


cellule_id = 14

print("=== PREMIER APPEL ===")

start = time.perf_counter()

result1 = get_cellule_by_id(cellule_id)

end = time.perf_counter()

print("Résultat :", result1)
print(f"Temps : {(end - start) * 1000:.2f} ms")


print("\n=== DEUXIÈME APPEL ===")

start = time.perf_counter()

result2 = get_cellule_by_id(cellule_id)

end = time.perf_counter()

print("Résultat :", result2)
print(f"Temps : {(end - start) * 1000:.2f} ms")


print("\n=== VÉRIFICATION REDIS ===")

cache_key = f"cellule:id:{cellule_id}"

cached = get_cache(cache_key)

print("Clé :", cache_key)
print("Cache :", cached)