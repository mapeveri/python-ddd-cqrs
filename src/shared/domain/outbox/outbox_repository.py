import abc
from typing import List, Protocol

from src.shared.domain.outbox.outbox import Outbox
from src.shared.domain.outbox.outbox_criteria import OutboxCriteria
from src.shared.domain.value_objects.outbox_id import OutboxId


class OutboxRepository(Protocol):
    @abc.abstractmethod
    def save(self, outbox: Outbox) -> None:
        ...

    @abc.abstractmethod
    def remove(self, outboxId: OutboxId) -> None:
        ...

    @abc.abstractmethod
    def find_by_criteria(self, criteria: OutboxCriteria) -> List[Outbox]:
        ...
