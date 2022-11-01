import abc
from typing import List

from src.shared.domain.outbox.outbox import Outbox
from src.shared.domain.value_objects.outbox_id import OutboxId


class OutboxRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def save(self, outbox: Outbox) -> None:
        ...

    @abc.abstractmethod
    def remove(self, outboxId: OutboxId) -> None:
        ...

    @abc.abstractmethod
    def find_by_order_by_created_at_asc(self) -> List[Outbox]:
        ...