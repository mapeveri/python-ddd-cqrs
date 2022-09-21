from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.zone import Zone
from src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.sqlalchemy_event import event_table
from src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.sqlalchemy_zone import zone_table
from src.shared.infrastructure.persistence.sqlalchemy.registry import mapper_registry


def mapper_event_context_tables():
    mapper_registry.map_imperatively(Event, event_table)
    mapper_registry.map_imperatively(Zone, zone_table)
