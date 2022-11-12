from typing import Type, Any, Dict

from src.shared.domain.bus.query.query import Query
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.domain.bus.query.query_handler import QueryHandler


class MemoryQueryBus(QueryBus):
    def __init__(self) -> None:
        self.handlers: Dict = {}

    def register(self, query: Type[Query], handler: Type[QueryHandler]) -> None:
        self.handlers[query.name()] = handler

    def ask(self, query: Query) -> Any:
        return self.handlers[query.name()](query)
