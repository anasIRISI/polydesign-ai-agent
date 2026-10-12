from app.cache.redis_cache import (
    ping_cache,
    get_cache,
    set_cache,
    delete_cache,
)


print("1. Test PING")

if ping_cache():
    print("Redis : OK")


print("\n2. Test SET")

set_cache(
    "test:cache",
    {
        "message": "Cache Polydesign fonctionne",
        "value": 123
    },
    ttl=60
)

print("SET : OK")


print("\n3. Test GET")

result = get_cache("test:cache")

print("Résultat :", result)


print("\n4. Test DELETE")

delete_cache("test:cache")

result = get_cache("test:cache")

print("Après suppression :", result)