from abc import ABC

from src.shared.domain.idempotence.idempotence_repository import IdempotenceRepository


class EmailIdempotenceRepository(IdempotenceRepository, ABC):
    pass
