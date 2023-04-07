from src.marketplace.event.application.command.update.update_event_command import UpdateEventCommand
from tests.shared.infrastructure.utils.Faker.faker import faker


class UpdateEventCommandMother:
    @staticmethod
    def create() -> UpdateEventCommand:
        return UpdateEventCommand(
            faker.random_int(),
            faker.unique.random_int(),
            faker.name(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            [],
        )
