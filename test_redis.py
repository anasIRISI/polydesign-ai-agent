import redis


client = redis.from_url(
    "redis://localhost:6379/0",
    decode_responses=True
)


print("Test connexion Redis...")

if client.ping():
    print("Redis connecté : OK")

client.set(
    "test_python",
    "Connexion Python réussie",
    ex=60
)

value = client.get("test_python")

print("Valeur récupérée :", value)