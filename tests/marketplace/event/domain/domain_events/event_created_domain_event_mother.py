from src.marketplace.event.domain.domain_events.event_created_domain_event import EventCreatedDomainEvent
from src.marketplace.event.domain.event import Event
from tests.marketplace.event.domain.value_objects import EventIdMother, ModeMother
from tests.shared.infrastructure.utils.Faker.faker import faker


class EventCreatedDomainEventMother:
    @staticmethod
    def create(data: dict = None) -> EventCreatedDomainEvent:
        event_created = EventCreatedDomainEvent(
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
            [],
        )

        if data:
            event_created = EventCreatedDomainEvent(
                data["id"],
                data["provider_id"],
                data["mode"],
                data["provider_organizer_company_id"],
                data["title"],
                data["start_date"],
                data["end_date"],
                data["sell_from"],
                data["sell_to"],
                data["sold_out"],
                data["zones"],
            )

        return event_created

    @staticmethod
    def create_from_event(event: Event) -> EventCreatedDomainEvent:
        return EventCreatedDomainEvent(
            str(event.id),
            event.provider_id,
            event.mode.value(),
            event.provider_organizer_company_id,
            event.title,
            event.start_date,
            event.end_date,
            event.sell_from,
            event.sell_to,
            event.sold_out,
            [],
        )
