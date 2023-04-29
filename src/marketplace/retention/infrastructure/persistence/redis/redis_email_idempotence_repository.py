from typing import ClassVar

from dependency_injector.wiring import Provide
from redis import Redis

from src.marketplace.retention.domain.email_idempotence_repository import EmailIdempotenceRepository
from src.shared.infrastructure.persistence.redis.redis_idempotence_repository import RedisIdempotenceRepository


class RedisEmailIdempotenceRepository(EmailIdempotenceRepository, RedisIdempotenceRepository):
    __EXPIRED_KEY: ClassVar[int] = 3600

    def __init__(self, redis: Redis = Provide["redis"]) -> None:
        super().__init__()
        self.__redis = redis
