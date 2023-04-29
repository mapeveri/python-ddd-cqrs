from typing import Any, Optional, ClassVar

from dependency_injector.wiring import Provide
from redis import Redis

from src.shared.domain.idempotence.idempotence_repository import IdempotenceRepository


class RedisIdempotenceRepository(IdempotenceRepository):
    __EXPIRED_KEY: ClassVar[int] = 3600

    def __init__(self, redis: Redis = Provide["redis"]) -> None:
        self.__redis = redis

    def get(self, key: str) -> Optional[Any]:
        return self.__redis.lrange(key, 0, -1)

    def set(self, key: str, value: Any) -> None:
        self.__redis.lpush(key, value)
        self.__redis.expire(key, self.__EXPIRED_KEY)
