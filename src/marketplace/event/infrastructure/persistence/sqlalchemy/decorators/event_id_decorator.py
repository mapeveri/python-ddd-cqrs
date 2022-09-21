from sqlalchemy.types import TypeDecorator, VARCHAR

from src.marketplace.event.domain.value_objects.event_id import EventId


class EventIdDecorator(TypeDecorator):
    impl = VARCHAR

    cache_ok = True

    def process_bind_param(self, event_id, dialect) -> str:
        if isinstance(event_id, str):
            return event_id

        if event_id is not None:
            return str(event_id)

    def process_result_value(self, value, dialect) -> EventId:
        if value is not None:
            return EventId(value)
