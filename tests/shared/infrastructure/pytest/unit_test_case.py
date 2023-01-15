import unittest
from typing import List
from unittest.mock import Mock

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.bus.event.event_bus import EventBus


class UnitTestCase(unittest.TestCase):
    event_bus = Mock(spec=EventBus)

    def should_publish_domain_events(self, event: List[DomainEvent]):
        self.event_bus.publish.assert_called_with(event)

    def should_not_publish_domain_events(self):
        self.event_bus.publish.assert_not_called()
