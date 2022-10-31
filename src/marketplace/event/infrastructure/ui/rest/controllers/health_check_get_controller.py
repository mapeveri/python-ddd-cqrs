from flask.views import View
from werkzeug.wrappers import Response


class HealthCheckGetController(View):
    methods = ['GET']

    def dispatch_request(self) -> Response:
        return "<p>OK</p>"
