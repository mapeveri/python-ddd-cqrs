from flask import Blueprint

from src.marketplace.event.infrastructure.ui.rest.views import health_check, create_event, get_events

blueprint = Blueprint("events_routes", __name__)


blueprint.add_url_rule("/", methods=["GET"], view_func=health_check)
blueprint.add_url_rule("/create-event", methods=["POST"], view_func=create_event)
blueprint.add_url_rule("/search", methods=["GET"], view_func=get_events)
