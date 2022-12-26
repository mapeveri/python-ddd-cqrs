from flask.views import View


class HealthCheckGetController(View):
    methods = ["GET"]

    def dispatch_request(self) -> str:
        return "<p>OK</p>"
