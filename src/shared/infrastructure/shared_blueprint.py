from typing import Optional, Tuple

import click
from flask import Flask, Blueprint

from src.shared.infrastructure.console.utils import add_commands

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
