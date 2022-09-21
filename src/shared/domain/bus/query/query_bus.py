from abc import ABC, abstractmethod
from typing import Type

from src.shared.domain.bus.query.query import Query
from src.shared.domain.bus.query.query_handler import QueryHandler


class QueryBus(ABC):
    @abstractmethod
    def register(self, query: Type[Query], handler: Type[QueryHandler]):
        pass

    @abstractmethod
    def ask(self, query: Query):
        pass
