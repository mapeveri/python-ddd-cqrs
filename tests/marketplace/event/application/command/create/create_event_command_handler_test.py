from src.marketplace.event.application.command.create.create_event_command_handler import CreateEventCommandHandler
from tests.marketplace.event.application.command.create.create_event_command_mother import CreateEventCommandMother
from tests.marketplace.event.domain.domain_events.event_created_domain_event_mother import EventCreatedDomainEventMother
from tests.marketplace.event.domain.event_mother import EventMother
from tests.marketplace.event.event_unit_test_case import EventUnitTestCase


class CreateEventCommandHandlerTest(EventUnitTestCase):
    SUT: CreateEventCommandHandler

    def setUp(self):
        super(CreateEventCommandHandlerTest, self).setUp()
        self.SUT = CreateEventCommandHandler(self.event_repository, self.event_bus)

    def test_should_create_an_event(self) -> None:
        command = CreateEventCommandMother.create()
        event = EventMother.create_from_create_event_command(command)
        event_created_domain_event = EventCreatedDomainEventMother.create_from_event(event)

        self.SUT(command)

        self.should_save_event(event)
        self.should_publish_domain_events([event_created_domain_event])
