from typing import List
from unittest.mock import Mock, MagicMock

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.zone import Zone
from src.marketplace.event.domain.zone_repository import ZoneRepository
from tests.shared.infrastructure.pytest.unit_test_case import UnitTestCase


class EventUnitTestCase(UnitTestCase):
    event_repository: EventRepository = Mock(spec=EventRepository)
    zone_repository: ZoneRepository = Mock(spec=ZoneRepository)

    def setUp(self):
        self.event_repository.save = MagicMock()
        self.event_repository.find_by_provider_id = MagicMock()
        self.zone_repository.zones_by_event_id = MagicMock()

    def should_save_event(self, event: Event):
        self.event_repository.save.assert_called_once_with(event)

    def should_find_event_by_provider_id(self, event: Event):
        self.event_repository.find_by_provider_id.return_value = event

    def should_call_event_by_provider_id(self, event: Event):
        self.event_repository.find_by_provider_id.assert_called_once_with(event.provider_id)

    def should_find_zones_by_event_id(self, zones: List[Zone]):
        self.zone_repository.zones_by_event_id.return_value = zones

    def should_call_zones_by_event_id(self, event: Event):
        self.zone_repository.zones_by_event_id.assert_called_once_with(event.id)
