import datetime
from typing import Tuple, Any, Optional

from flask import jsonify, request
from flask.views import View
from prometheus_client import Summary

from src.marketplace.event.application.query.search_events.search_events_query import (
    SearchEventsQuery,
)
from src.shared.domain.exceptions.invalid_parameter_exception import InvalidParameterException
from src.shared.infrastructure.api_controller import ApiController

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


class EventsGetController(View, ApiController):
    methods = ["GET"]

    @REQUEST_TIME.time()
    def dispatch_request(self) -> Tuple[Any, int]:
        try:
            args = request.args
            start_date: Optional[str] = args.get("starts_at")
            end_date: Optional[str] = args.get("ends_at")
            self.__check_dates(start_date, end_date)

            events = self.query_bus.ask(SearchEventsQuery(start_date, end_date))
            response = jsonify({"data": {"events": events}, "error": None})
            code = 200
        except InvalidParameterException as e:
            code = 400
            response = jsonify({"data": None, "error": {"code": code, "message": str(e)}})
        except Exception as e:
            code = 500
            response = jsonify({"data": None, "error": {"code": code, "message": str(e)}})

        return response, code

    def __check_dates(self, start_date: Optional[str], end_date: Optional[str]) -> None:
        if start_date and end_date:
            try:
                datetime.datetime.fromisoformat(start_date.rstrip("Z") + "+00:00")
                datetime.datetime.fromisoformat(end_date.rstrip("Z") + "+00:00")
            except Exception:
                raise InvalidParameterException("Invalid value in parameters")
