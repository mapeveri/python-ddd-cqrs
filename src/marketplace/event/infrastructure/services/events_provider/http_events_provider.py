from typing import List

import requests


class HttpEventsProvider:
    EVENT_PROVIDER = "https://634160d520f1f9d79971c33a.mockapi.io/api/events"

    def __call__(self) -> List:
        response = requests.get(self.EVENT_PROVIDER)
        return response.json()
