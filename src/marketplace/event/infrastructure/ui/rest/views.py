from typing import Tuple, Any

from flask import jsonify, request
from werkzeug.wrappers import Response

from src.marketplace.event.infrastructure.ui.rest.controllers.events_get_controller import EventsGetController
from src.marketplace.event.infrastructure.ui.rest.controllers.events_post_controller import EventsPostController
from src.shared.domain.exceptions import InvalidParameter

events_get_controller = EventsGetController()
events_post_controller = EventsPostController()


def health_check() -> Response:
    return "<p>OK</p>"


def create_event() -> Tuple[Any, int]:
    try:
        events_post_controller(request.json)
        response = jsonify({"data": "OK"})
        code = 201
    except Exception as e:
        code = 500
        response = jsonify({"data": None, "error": {
            "code": code,
            "message": str(e)
        }})

    return response, code


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
