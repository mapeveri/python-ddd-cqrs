class EventNotFoundException(Exception):
    def __init__(self, event_provider_id: int) -> None:
        self.event_provider_id = event_provider_id
        super().__init__(f"Event with provider id {str(event_provider_id)} not exists")
