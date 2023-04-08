from flask import Flask

from src.marketplace.event.infrastructure import event_blueprint
from src.shared.infrastructure import shared_blueprint


class MarketplaceApp:
    def __init__(self, app: Flask) -> None:
        self.app = app

    def setup_app(self) -> None:
        self.app.register_blueprint(event_blueprint.blueprint, url_prefix="/api/v1")
        self.app.register_blueprint(shared_blueprint.blueprint)
