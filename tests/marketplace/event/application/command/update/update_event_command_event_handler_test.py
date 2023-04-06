from src.marketplace.event.application.command.update.update_event_command_handler import UpdateEventCommandHandler
from tests.marketplace.event.application.command.update.update_event_command_mother import UpdateEventCommandMother
from tests.marketplace.event.domain.domain_events.event_updated_domain_event_mother import EventUpdatedDomainEventMother
from tests.marketplace.event.domain.event_mother import EventMother
from tests.marketplace.event.event_unit_test_case import EventUnitTestCase


class UpdateEventCommandHandlerTest(EventUnitTestCase):
    def setUp(self):
        super(UpdateEventCommandHandlerTest, self).setUp()
        self.SUT = UpdateEventCommandHandler(
            self.event_repository,
            self.zone_repository,
            self.unit_of_work,
            self.event_bus
        )

    def test_should_update_an_event(self) -> None:
        command = UpdateEventCommandMother.create()
        event = EventMother.create_from_update_event_command(command)
        event_updated_domain_event = EventUpdatedDomainEventMother.create_from_event(event)

        self.should_find_event_by_provider_id(event)
        self.should_find_zones_by_event_id(event.zones)

        self.SUT(command)

        self.should_call_event_by_provider_id(event)
        self.should_call_zones_by_event_id(event)
        self.should_save_event(event)
        self.should_publish_domain_events([event_updated_domain_event])
