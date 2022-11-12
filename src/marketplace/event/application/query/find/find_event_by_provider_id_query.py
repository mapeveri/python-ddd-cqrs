from dataclasses import dataclass

from src.shared.domain.bus.query.query import Query


@dataclass(frozen=True)
class FindEventByProviderIdQuery(Query):
    provider_id: int
