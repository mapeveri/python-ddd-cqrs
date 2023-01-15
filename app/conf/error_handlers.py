import logging
from http import HTTPStatus

from flask import Flask as FlaskApp, Response

from src.shared.domain.exceptions.generic_error_exception import GenericErrorException

logger = logging.getLogger("marketplace")


def configure(app: FlaskApp) -> None:
    app.register_error_handler(Exception, lambda e: handle_generic_error(e))


def handle_generic_error(e: Exception) -> Response:
    logger.exception(str(e))

    error = GenericErrorException(repr(e))
    return {"error": {"code": "GENERIC_ERROR", "message": str(error)}, "data": None}, HTTPStatus.INTERNAL_SERVER_ERROR
