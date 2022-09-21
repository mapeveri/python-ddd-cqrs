import unittest
from typing import List
from unittest.mock import Mock, MagicMock

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.bus.event.event_bus import EventBus


class UnitTestCase(unittest.TestCase):
    event_bus: EventBus = Mock(spec=EventBus)

    def setUp(self):
        self.event_bus.publish = MagicMock()

    def should_publish_domain_events(self, event: List[DomainEvent]):
        self.event_bus.publish.assert_called_with(event)
