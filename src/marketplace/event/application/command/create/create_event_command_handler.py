from src.marketplace.event.application.command.create.create_event_command import (
    CreateEventCommand,
)
from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.exceptions.event_already_exists_exception import EventAlreadyExistsException
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.datetime_utils import ensure_datetime_iso_is_valid


class CreateEventCommandHandler(CommandHandler):
    def __init__(self, event_repository: EventRepository, event_bus: EventBus) -> None:
        self.__event_repository = event_repository
        self.__event_bus = event_bus

    def __call__(self, command: CreateEventCommand) -> None:
        event_id = EventId(command.id)
        self.__check_event_does_not_exists(event_id)

        provider_id = command.provider_id
        mode = Mode(command.mode)
        provider_organizer_company_id = command.provider_organizer_company_id
        title = command.title

        start_date = ensure_datetime_iso_is_valid(command.start_date)
        end_date = ensure_datetime_iso_is_valid(command.end_date)
        sell_from = ensure_datetime_iso_is_valid(command.sell_from)
        sell_to = ensure_datetime_iso_is_valid(command.sell_to)

        sold_out = command.sold_out
        zones = command.zones

        event = Event.create(
            event_id,
            provider_id,
            mode,
            provider_organizer_company_id,
            title,
            start_date,
            end_date,
            sell_from,
            sell_to,
            sold_out,
            zones,
        )

        self.__event_repository.save(event)

        self.__event_bus.publish(event.pull_domain_events())

    def __check_event_does_not_exists(self, event_id: EventId) -> None:
        event = self.__event_repository.find_by_id(event_id)
        if event is not None:
            raise EventAlreadyExistsException(event_id)
