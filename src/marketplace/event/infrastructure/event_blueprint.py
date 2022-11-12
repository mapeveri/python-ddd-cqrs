from flask import Blueprint

from src.marketplace.event.infrastructure.ui.rest.controllers.events_get_controller import (
    EventsGetController,
)
from src.marketplace.event.infrastructure.ui.rest.controllers.events_post_controller import (
    EventsPostController,
)
from src.marketplace.event.infrastructure.ui.rest.controllers.health_check_get_controller import (
    HealthCheckGetController,
)

blueprint = Blueprint("events_routes", __name__)


blueprint.add_url_rule("/", view_func=HealthCheckGetController.as_view("health_check"))
blueprint.add_url_rule("/search", view_func=EventsGetController.as_view("get_events"))
blueprint.add_url_rule("/create-event", view_func=EventsPostController.as_view("create_event"))
