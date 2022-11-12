from flask import Blueprint

from src.shared.infrastructure.console.commands.publish_events_domain_console_command import (
    publish_events_console_command,
)

blueprint = Blueprint("shared", __name__)

blueprint.cli.add_command(publish_events_console_command)
