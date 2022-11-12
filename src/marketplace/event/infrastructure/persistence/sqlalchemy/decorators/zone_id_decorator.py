from typing import Any, Optional

from sqlalchemy.types import TypeDecorator, VARCHAR

from src.marketplace.event.domain.value_objects.zone_id import ZoneId


class ZoneIdDecorator(TypeDecorator):
    impl = VARCHAR

    cache_ok = True

    def process_bind_param(self, zone_id: Any, dialect: Any) -> Optional[str]:
        if isinstance(zone_id, str):
            return str(zone_id)

        if zone_id is not None:
            return str(zone_id)

        return None

    def process_result_value(self, value: Any, dialect: Any) -> Optional[ZoneId]:
        if value is not None:
            return ZoneId(value)

        return None
