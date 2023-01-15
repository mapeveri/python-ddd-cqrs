from src.marketplace.event.domain.value_objects.event_id import EventId


class EventAlreadyExistsException(Exception):
    def __init__(self, event_id: EventId) -> None:
        self.event_id = event_id
        super().__init__(f"Event with id {str(event_id)} already exists")
