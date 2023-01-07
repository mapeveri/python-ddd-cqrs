from typing import List

from dependency_injector.wiring import inject, Provide
from flask_mail import Mail, Message

from src.marketplace.retention.domain.send_email import SendEmail


class FlaskSendEmail(SendEmail):
    @inject
    def __init__(self, sender: str, recipients: List[str], mail: Mail = Provide["mail"]) -> None:
        self.__sender = sender
        self.__recipients = recipients
        self.__mail = mail

    def send(self, title: str, content: str) -> None:
        msg = Message(title, sender=self.__sender, recipients=self.__recipients)
        msg.body = content
        self.__mail.send(msg)
