from typing import List
from unittest.mock import Mock, MagicMock

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.zone import Zone
from src.marketplace.event.domain.zone_repository import ZoneRepository
from src.shared.domain.unit_of_work import UnitOfWork
from tests.shared.infrastructure.pytest.unit_test_case import UnitTestCase


class EventUnitTestCase(UnitTestCase):
    def setUp(self):
        self.event_repository = Mock(spec=EventRepository)
        self.zone_repository = Mock(spec=ZoneRepository)
        self.unit_of_work = MagicMock(spec=UnitOfWork)
        self.event_bus.reset_mock()

    def should_find_by_id(self, event: Event) -> None:
        self.event_repository.find_by_id.return_value = event

    def should_not_find_by_id(self) -> None:
        self.event_repository.find_by_id.return_value = None

    def should_save_event(self, event: Event):
        self.event_repository.save.assert_called_once_with(event)

    def should_not_save_event(self):
        self.event_repository.save.assert_not_called()

    def should_find_event_by_provider_id(self, event: Event):
        self.event_repository.find_by_provider_id.return_value = event

    def should_call_event_by_provider_id(self, event: Event):
        self.event_repository.find_by_provider_id.assert_called_once_with(event.provider_id)

    def should_find_zones_by_event_id(self, zones: List[Zone]):
        self.zone_repository.zones_by_event_id.return_value = zones

    def should_call_zones_by_event_id(self, event: Event):
        self.zone_repository.zones_by_event_id.assert_called_once_with(event.id)
