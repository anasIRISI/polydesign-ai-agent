import json
import os

import redis


REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379/0"
)


redis_client = redis.from_url(
    REDIS_URL,
    decode_responses=True
)


def get_cache(key: str):
    value = redis_client.get(key)

    if value is None:
        return None

    return json.loads(value)


def set_cache(key: str, value, ttl: int = 300):
    redis_client.setex(
        key,
        ttl,
        json.dumps(
            value,
            ensure_ascii=False,
            default=str
        )
    )


def delete_cache(key: str):
    redis_client.delete(key)


def clear_cache():
    redis_client.flushdb()


def ping_cache():
    return redis_client.ping()