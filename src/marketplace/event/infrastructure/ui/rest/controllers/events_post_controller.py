from typing import Tuple, Any, Dict, List

from flask import jsonify, request
from flask.views import View

from src.marketplace.event.application.command.create.create_event_command import (
    CreateEventCommand,
)
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.zone_id import ZoneId
from src.shared.infrastructure.api_controller import ApiController


class EventsPostController(View, ApiController):
    methods = ["POST"]

    def dispatch_request(self) -> Tuple[Any, int]:
        try:
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

            self.command_bus.dispatch(
                CreateEventCommand(
                    EventId.next(),
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

            response = jsonify({"data": "OK"})
            code = 201
        except Exception as e:
            code = 500
            response = jsonify({"data": None, "error": {"code": code, "message": str(e)}})

        return response, code
