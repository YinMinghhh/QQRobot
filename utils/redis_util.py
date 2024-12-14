import redis

class RedisUtil:
    __slots__=(
        "client"
    )

    def __init__(self, host="localhost", port=6379, db=0, decode_responses=True):
        self.client = redis.StrictRedis(
            host=host,
            port=port,
            db = db,
            decode_responses=decode_responses
        )

    def set_key(self, key: str, value: str, expire=None) -> None:
        self.client.set(key, value, ex=expire)

    def _get_key(self, key: str):
        return self.client.get(key)

    def key_exists(self, key: str) -> bool:
        return self.client.exists(key) > 0

    def get_ttl(self, key):
        return self.client.ttl(key)

redis_util = RedisUtil()
