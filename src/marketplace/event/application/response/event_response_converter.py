import datetime
from typing import List

from src.marketplace.event.application.response.event_response import EventResponse


class EventResponseConverter:
    def convert(self, data: List) -> List[EventResponse]:
        return list(map(self.__event_response, data))

    def __event_response(self, event_data: dict) -> EventResponse:
        event = event_data["_source"]
        start_date = datetime.datetime.fromisoformat(event["start_date"])
        end_date = datetime.datetime.fromisoformat(event["end_date"])

        return EventResponse(
            event["id"],
            event["title"],
            start_date.strftime("%Y-%m-%d"),
            start_date.strftime("%H:%M:%S"),
            end_date.strftime("%Y-%m-%d"),
            end_date.strftime("%H:%M:%S"),
            event["min_price"],
            event["max_price"],
        )
