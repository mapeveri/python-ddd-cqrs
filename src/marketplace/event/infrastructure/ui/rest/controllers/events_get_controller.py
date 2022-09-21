import datetime

from src.marketplace.event.application.query.search_events.search_events_query import SearchEventsQuery
from src.shared.domain.exceptions import InvalidParameter
from src.shared.infrastructure.api_controller import ApiController


class EventsGetController(ApiController):
    def __call__(self, args):
        start_date = args.get('starts_at')
        end_date = args.get('ends_at')
        self._validate_dates(start_date, end_date)
        return self.query_bus.ask(SearchEventsQuery(start_date, end_date))

    def _validate_dates(self, start_date: str, end_date: str):
        if start_date and end_date:
            try:
                datetime.datetime.fromisoformat(start_date.rstrip('Z') + '+00:00')
                datetime.datetime.fromisoformat(end_date.rstrip('Z') + '+00:00')
            except Exception:
                raise InvalidParameter('Invalid value in parameters')
