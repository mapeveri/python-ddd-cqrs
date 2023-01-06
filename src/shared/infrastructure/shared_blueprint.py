from typing import Optional, Tuple

import click
from flask import Blueprint

from src.shared.infrastructure.console.utils import add_commands
from src.shared.infrastructure.security.http_auth import auth
from src.shared.infrastructure.ui.rest.controllers.health_check_get_controller import HealthCheckGetController
from src.shared.infrastructure.ui.rest.controllers.metrics_get_controller import MetricsGetController

blueprint = Blueprint("shared", __name__)


def _commands() -> Optional[Tuple]:
    return (
        (
            "publish-domain-events-console-command",
            "src.shared.infrastructure.console.commands.publish_domain_events_cli.PublishDomainEventsCli",
            (click.option("--limit", type=click.INT, required=False),),
        ),
    )


add_commands(blueprint, _commands())

blueprint.add_url_rule("/", view_func=HealthCheckGetController.as_view("health_check"))
blueprint.add_url_rule("/metrics", view_func=auth.login_required(MetricsGetController.as_view("metrics")))
