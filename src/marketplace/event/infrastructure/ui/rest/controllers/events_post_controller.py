from http import HTTPStatus
from typing import Tuple, Any, Dict, List

from flask import request
from flask.views import View

from src.marketplace.event.application.command.create.create_event_command import (
    CreateEventCommand,
)
from src.marketplace.event.domain.exceptions.event_already_exists_exception import EventAlreadyExistsException
from src.marketplace.event.domain.value_objects.zone_id import ZoneId
from src.shared.infrastructure.api_controller import ApiController


class EventsPostController(View, ApiController):
    methods = ["POST"]

    def dispatch_request(self, event_id: str) -> Tuple[Any, int]:
        """
        Create event
        ---
        consumes:
            - application/json
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: Event
              required:
                - name
              properties:
                title:
                  type: string
                  description: Event title
                mode:
                  type: string
                  description: Event mode
                  example: Online
                provider_id:
                  type: number
                  description: Provider id
                provider_organizer_company_id:
                  type: number
                  description: Provider organizer company id
                start_date:
                  type: string
                  description: Start date event
                end_date:
                  type: string
                  description: End date event
                sell_from:
                  type: string
                  description: Sell from date event
                sell_to:
                  type: string
                  description: Sell to date event
                sold_out:
                  type: boolean
                  description: Event sold out
                zones:
                  description: Zones related to the event
                  type: array
                  items:
                    properties:
                        provider_zone_id:
                            type: number
                            description: Provider zone id
                        capacity:
                            type: number
                            description: Event zone capacity
                        price:
                            type: number
                            description: Event price
                        name:
                            type: string
                            description: Zone name
                        numbered:
                            type: boolean
                            description: Zone is numbered
        response:
          201:
            description: Event created
          400:
            description: Bad request
          500:
            description: Unexpected error.
        """
        content: Dict = request.json

        zones: List[Dict] = []
        for zone in content["zones"]:
            zones.append(
                {
                    "id": ZoneId.next(),
                    "provider_zone_id": zone["provider_zone_id"],
                    "capacity": zone["capacity"],
                    "price": zone["price"],
                    "name": zone["name"],
                    "numbered": zone["numbered"],
                }
            )

        try:
            self.command_bus.dispatch(
                CreateEventCommand(
                    event_id,
                    content["provider_id"],
                    content["mode"],
                    content["provider_organizer_company_id"],
                    content["title"],
                    content["start_date"],
                    content["end_date"],
                    content["sell_from"],
                    content["sell_to"],
                    content["sold_out"],
                    zones,
                )
            )
        except EventAlreadyExistsException as e:
            return {
                "error": {"code": "EVENT_ALREADY_EXISTS", "message": str(e)},
                "data": None,
            }, HTTPStatus.BAD_REQUEST

        return {}, HTTPStatus.CREATED
