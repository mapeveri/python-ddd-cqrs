from src.marketplace.event.application.command.create.create_event_command import CreateEventCommand
from tests.marketplace.event.domain.value_objects import EventIdMother, ModeMother
from tests.shared.infrastructure.utils.Faker.faker import faker


class CreateEventCommandMother:
    @staticmethod
    def create() -> CreateEventCommand:
        return CreateEventCommand(
            str(EventIdMother.create()),
            faker.random_int(),
            ModeMother.create().value(),
            faker.unique.random_int(),
            faker.name(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            []
        )
