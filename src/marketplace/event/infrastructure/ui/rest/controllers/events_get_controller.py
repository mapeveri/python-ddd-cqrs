import datetime
from typing import Tuple, Any

from flask import jsonify, request
from flask.views import View

from src.marketplace.event.application.query.search_events.search_events_query import SearchEventsQuery
from src.shared.domain.exceptions import InvalidParameter
from src.shared.infrastructure.api_controller import ApiController


class EventsGetController(View, ApiController):
    methods = ['GET']

    def dispatch_request(self) -> Tuple[Any, int]:
        try:
            args = request.args
            start_date = args.get('starts_at')
            end_date = args.get('ends_at')
            self.__validate_dates(start_date, end_date)
            events = self.query_bus.ask(SearchEventsQuery(start_date, end_date))
            response = jsonify({"data": {"events": events}, "error": None})
            code = 200
        except InvalidParameter as e:
            code = 400
            response = jsonify({"data": None, "error": {
                "code": code,
                "message": str(e)
            }})
        except Exception as e:
            code = 500
            response = jsonify({"data": None, "error": {
                "code": code,
                "message": str(e)
            }})

        return response, code

    def __validate_dates(self, start_date: str, end_date: str):
        if start_date and end_date:
            try:
                datetime.datetime.fromisoformat(start_date.rstrip('Z') + '+00:00')
                datetime.datetime.fromisoformat(end_date.rstrip('Z') + '+00:00')
            except Exception:
                raise InvalidParameter('Invalid value in parameters')
