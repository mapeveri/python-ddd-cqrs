from typing import Any, Optional

from sqlalchemy.types import TypeDecorator, VARCHAR

from src.marketplace.event.domain.value_objects.event_id import EventId


class EventIdDecorator(TypeDecorator):
    impl = VARCHAR

    cache_ok = True

    def process_bind_param(self, event_id: Any, dialect: Any) -> Optional[str]:
        if isinstance(event_id, str):
            return event_id

        if event_id is not None:
            return str(event_id)

        return None

    def process_result_value(self, value: Any, dialect: Any) -> Optional[EventId]:
        if value is not None:
            return EventId(value)

        return None
