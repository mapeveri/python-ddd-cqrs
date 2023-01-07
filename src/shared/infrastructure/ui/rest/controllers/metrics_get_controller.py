from flask import Response
from flask.views import View
from prometheus_client import multiprocess
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST


class MetricsGetController(View):
    methods = ["GET"]

    def dispatch_request(self) -> str:
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        data = generate_latest(registry)

        response_headers = [("Content-type", CONTENT_TYPE_LATEST), ("Content-Length", str(len(data)))]

        return Response(response=data, status=200, headers=response_headers)
