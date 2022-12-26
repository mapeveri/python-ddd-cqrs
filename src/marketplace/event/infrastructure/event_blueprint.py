from flask import Blueprint

from src.marketplace.event.infrastructure.ui.rest.controllers.events_get_controller import (
    EventsGetController,
)
from src.marketplace.event.infrastructure.ui.rest.controllers.events_post_controller import (
    EventsPostController,
)
from src.marketplace.event.infrastructure.ui.rest.controllers.upload_file_post_controller import (
    UploadFilePostController,
)

blueprint = Blueprint("events_routes", __name__)


blueprint.add_url_rule("/search", view_func=EventsGetController.as_view("get_events"))
blueprint.add_url_rule("/create-event", view_func=EventsPostController.as_view("create_event"))
blueprint.add_url_rule("/upload-file", view_func=UploadFilePostController.as_view("upload_file"))
