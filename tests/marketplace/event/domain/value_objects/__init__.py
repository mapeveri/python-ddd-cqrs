import uuid

from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode


class EventIdMother:
    @staticmethod
    def create(event_id_value: str = None) -> EventId:
        event_id = EventId(str(uuid.uuid4()))

        if event_id_value:
            event_id = EventId(event_id_value)

        return event_id


class ModeMother:
    @staticmethod
    def create(mode_value: str = None) -> Mode:
        mode = Mode("online")

        if mode_value:
            mode = Mode(mode_value)

        return mode
