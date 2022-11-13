from flask import Blueprint

from src.shared.infrastructure.console.commands.publish_domain_events_cli import PublishDomainEventsCli

blueprint = Blueprint("shared", __name__)


blueprint.cli.add_command(PublishDomainEventsCli)
