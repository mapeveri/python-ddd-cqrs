from typing import Type

from src.shared.domain.bus.query.query import Query
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.domain.bus.query.query_handler import QueryHandler


class MemoryQueryBus(QueryBus):
    def __init__(self):
        self.handlers = {}

    def register(self, query: Type[Query], handler: Type[QueryHandler]):
        self.handlers[query.name()] = handler

    def ask(self, query: Query):
        return self.handlers[query.name()](query)
