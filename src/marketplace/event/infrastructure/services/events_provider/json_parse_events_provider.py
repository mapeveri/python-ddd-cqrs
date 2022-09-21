from xml.etree.ElementTree import Element

from src.marketplace.event.domain.value_objects.zone_id import ZoneId


class JsonParseEventsProvider:
    def __call__(self, events_data: list) -> list:
        events = []
        events_values = list(map(lambda event_element: event_element, events_data))
        for event in events_values:
            sell_mode = event['sell_mode'].lower()
            if sell_mode != 'online':
                continue

            title = event['title']
            provider_organizer_company_id = event.get('organizer_company_id', False)
            provider_event_id = int(event['base_event_id'])
            sell_mode = event['sell_mode'].lower()

            event_attributes = event['event']
            event_start_date = event_attributes['event_start_date']
            event_end_date = event_attributes['event_end_date']
            sell_from = event_attributes['sell_from']
            sell_to = event_attributes['sell_to']
            sold_out = bool(event_attributes['sold_out'])

            zones = event_attributes['zone']
            zones_list = list(map(self._zones, zones))

            events.append({
                'provider_event_id': provider_event_id,
                'provider_organizer_company_id': provider_organizer_company_id,
                'title': title,
                'sell_mode': sell_mode,
                'event_start_date': event_start_date,
                'event_end_date': event_end_date,
                'sell_from': sell_from,
                'sell_to': sell_to,
                'sold_out': sold_out,
                'zones': zones_list,
            })

        return events

    def _zones(self, zone) -> dict:
        zone_id = int(zone['zone_id'])
        capacity = int(zone['capacity'])
        price = float(zone['price'])
        name = zone['name']
        numbered = bool(zone['numbered'])

        return {
            'id': ZoneId.next(),
            'provider_zone_id': zone_id,
            'capacity': capacity,
            'price': price,
            'name': name,
            'numbered': numbered
        }
