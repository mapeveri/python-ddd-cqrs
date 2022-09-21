from src.marketplace.event.domain.domain_events.event_updated_domain_event import EventUpdatedDomainEvent
from src.marketplace.event.domain.event import Event
from tests.marketplace.event.domain.value_objects import EventIdMother, ModeMother
from tests.shared.infrastructure.utils.Faker.faker import faker


class EventUpdatedDomainEventMother:
    @staticmethod
    def create(data: dict = None) -> EventUpdatedDomainEvent:
        event_updated = EventUpdatedDomainEvent(
            str(EventIdMother.create()),
            faker.random_int(),
            faker.unique.random_int(),
            ModeMother.create().value(),
            faker.name(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            faker.date_time().isoformat(),
            []
        )

        if data:
            event_updated = EventUpdatedDomainEvent(
                data['id'],
                data['provider_id'],
                data['mode'],
                data['provider_organizer_company_id'],
                data['title'],
                data['start_date'],
                data['end_date'],
                data['sell_from'],
                data['sell_to'],
                data['sold_out'],
                data['zones']
            )

        return event_updated

    @staticmethod
    def create_from_event(event: Event) -> EventUpdatedDomainEvent:
        return EventUpdatedDomainEvent(
            str(event.id),
            event.provider_id,
            event.provider_organizer_company_id,
            event.mode.value(),
            event.title,
            event.start_date,
            event.end_date,
            event.sell_from,
            event.sell_to,
            event.sold_out,
            [],
        )
