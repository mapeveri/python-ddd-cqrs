from typing import Tuple, Any

from flask import Blueprint, jsonify, request
from werkzeug.wrappers import Response

from src.marketplace.event.infrastructure.ui.rest.controllers.events_get_controller import EventsGetController
from src.shared.domain.exceptions import InvalidParameter

blueprint = Blueprint("events_routes", __name__)

events_get_controller = EventsGetController()


@blueprint.route("/")
def health_check() -> Response:
    return "<p>OK</p>"


@blueprint.route("/search", methods=["GET"])
def get_events() -> Tuple[Any, int]:
    try:
        events = events_get_controller(request.args)
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
