from src.marketplace.event.application.command.create.create_event_command_handler import CreateEventCommandHandler
from src.marketplace.event.domain.exceptions.event_already_exists_exception import EventAlreadyExistsException
from tests.marketplace.event.application.command.create.create_event_command_mother import CreateEventCommandMother
from tests.marketplace.event.domain.domain_events.event_created_domain_event_mother import EventCreatedDomainEventMother
from tests.marketplace.event.domain.event_mother import EventMother
from tests.marketplace.event.event_unit_test_case import EventUnitTestCase


class CreateEventCommandHandlerTest(EventUnitTestCase):
    def setUp(self):
        super(CreateEventCommandHandlerTest, self).setUp()
        self.SUT = CreateEventCommandHandler(self.event_repository, self.event_bus)

    def test_should_not_create_an_event_duplicated(self) -> None:
        command = CreateEventCommandMother.create()
        event = EventMother.create_from_create_event_command(command)

        self.should_find_by_id(event)

        with self.assertRaises(EventAlreadyExistsException):
            self.SUT(command)

        self.should_not_save_event()
        self.should_not_publish_domain_events()

    def test_should_create_an_event(self) -> None:
        command = CreateEventCommandMother.create()
        event = EventMother.create_from_create_event_command(command)
        event_created_domain_event = EventCreatedDomainEventMother.create_from_event(event)

        self.should_not_find_by_id()

        self.SUT(command)

        self.should_save_event(event)
        self.should_publish_domain_events([event_created_domain_event])
