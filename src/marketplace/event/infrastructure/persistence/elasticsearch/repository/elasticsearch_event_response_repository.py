from dataclasses import dataclass

from dependency_injector.wiring import Provide
from elasticsearch import Elasticsearch

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_reponse_repository import (
    EventResponseRepository,
)


@dataclass
class ElasticsearchEventResponseRepository(EventResponseRepository):
    es: Elasticsearch = Provide["es"]
    index = "events"

    def save(self, event: Event) -> None:
        prices = event.calculate_prices()
        event_id = str(event.id)
        doc = {
            "id": event_id,
            "title": event.title,
            "mode": event.mode.value(),
            "provider_id": event.provider_id,
            "provider_organizer_company_id": event.provider_organizer_company_id,
            "start_date": event.start_date,
            "end_date": event.end_date,
            "sell_from": event.sell_from,
            "sell_to": event.sell_to,
            "sold_out": event.sold_out,
            "min_price": prices["min_price"],
            "max_price": prices["max_price"],
        }

        self.es.update(index=self.index, id=event_id, body={"doc": doc, "doc_as_upsert": True})

    def search(self, start_date: str, end_date: str) -> list:
        params = {"sort": "start_date:asc"}

        if start_date and end_date:
            resp = self.es.search(
                index=self.index,
                params=params,
                query={
                    "bool": {
                        "must": [
                            {"range": {"start_date": {"gte": start_date, "lte": end_date}}},
                            {"range": {"end_date": {"gte": start_date, "lte": end_date}}},
                        ]
                    }
                },
            )
            return resp["hits"]["hits"]

        resp = self.es.search(index=self.index, query={"match_all": {}}, params=params)
        return resp["hits"]["hits"]
