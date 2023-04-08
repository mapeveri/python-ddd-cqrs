from src.shared.infrastructure.bus.command_bus_register import register_commands
from src.shared.infrastructure.bus.query_bus_register import register_queries


def configure_buses() -> None:
    register_commands()
    register_queries()
