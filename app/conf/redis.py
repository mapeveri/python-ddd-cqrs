from flask import Flask
from redis import Redis


def configure_redis(app: Flask) -> Redis:
    return Redis(host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"], decode_responses=True)
