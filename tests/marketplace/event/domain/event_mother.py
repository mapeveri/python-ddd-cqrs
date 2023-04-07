from datetime import datetime

from src.marketplace.event.application.command.create.create_event_command import CreateEventCommand
from src.marketplace.event.application.command.update.update_event_command import UpdateEventCommand
from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode
from tests.marketplace.event.domain.value_objects import EventIdMother, ModeMother
from tests.shared.infrastructure.utils.Faker.faker import faker


class EventMother:
    @staticmethod
    def create(data: dict = None) -> Event:
        event = Event(
            EventIdMother.create(),
            faker.random_int(),
            ModeMother.create(),
            faker.unique.random_int(),
            faker.name(),
            faker.date_time(),
            faker.date_time(),
            faker.date_time(),
            faker.date_time(),
            faker.date_time(),
            [],
        )

        if data:
            event = Event(
                EventId(data["id"]),
                data["provider_id"],
                Mode(data["mode"]),
                data["provider_organizer_company_id"],
                data["title"],
                data["start_date"],
                data["end_date"],
                data["sell_from"],
                data["sell_to"],
                data["sold_out"],
                data["zones"],
            )

        return event

    @staticmethod
    def create_from_create_event_command(command: CreateEventCommand):
        return Event(
            EventIdMother.create(command.id),
            command.provider_id,
            ModeMother.create(command.mode),
            command.provider_organizer_company_id,
            command.title,
            datetime.fromisoformat(command.start_date),
            datetime.fromisoformat(command.end_date),
            datetime.fromisoformat(command.sell_from),
            datetime.fromisoformat(command.sell_to),
            command.sold_out,
            command.zones,
        )

    @staticmethod
    def create_from_update_event_command(command: UpdateEventCommand):
        return Event(
            EventIdMother.create(),
            command.provider_id,
            ModeMother.create(),
            command.provider_organizer_company_id,
            command.title,
            datetime.fromisoformat(command.start_date),
            datetime.fromisoformat(command.end_date),
            datetime.fromisoformat(command.sell_from),
            datetime.fromisoformat(command.sell_to),
            command.sold_out,
            command.zones,
        )
