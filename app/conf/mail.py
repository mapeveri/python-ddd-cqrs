from flask import Flask
from flask_mail import Mail


def configure_mail(app: Flask) -> Mail:
    return Mail(app)
