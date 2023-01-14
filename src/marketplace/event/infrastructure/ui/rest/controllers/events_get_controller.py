import datetime
from typing import Tuple, Any, Optional

from flask import jsonify, request
from flask.views import View

from src.shared.infrastructure.prometheus.metrics import api_request_duration, QUANTILE
from src.marketplace.event.application.query.search_events.search_events_query import (
    SearchEventsQuery,
)
from src.shared.domain.exceptions.invalid_parameter_exception import InvalidParameterException
from src.shared.infrastructure.api_controller import ApiController


class EventsGetController(View, ApiController):
    methods = ["GET"]

    def dispatch_request(self) -> Tuple[Any, int]:
        """
        Search events
        ---
        parameters:
          - in: query
            name: starts_at
            type: string
            required: false
          - in: query
            name: ends_at
            type: string
            required: false
        responses:
          200:
            description: List of events
            schema:
              id: Event
              type: array
              items:
                  properties:
                    id:
                      type: string
                      description: Identification event
                    title:
                      type: string
                      description: Event title
                    max_price:
                      type: number
                      description: Max price event
                    min_price:
                      type: number
                      description: Min price event
                    start_date:
                      type: string
                      description: Date start at the event
                    start_time:
                      type: string
                      description: Date start time the event
                    end_date:
                      type: string
                      description: Date end at the event
                    end_time:
                      type: string
                      description: Date end time the event
          400:
            description: Bad request. Invalid parameters
          500:
            description: Unexpected error.
        """
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

        api_request_duration.labels(endpoint="get_events").observe(QUANTILE)
        return response, code

    def __check_dates(self, start_date: Optional[str], end_date: Optional[str]) -> None:
        if start_date and end_date:
            try:
                datetime.datetime.fromisoformat(start_date.rstrip("Z") + "+00:00")
                datetime.datetime.fromisoformat(end_date.rstrip("Z") + "+00:00")
            except Exception:
                raise InvalidParameterException("Invalid value in parameters")
