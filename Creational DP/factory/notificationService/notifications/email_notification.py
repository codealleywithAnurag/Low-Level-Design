from notifications.i_notification import INotification
from services.email_service import EmailService

class EmailNotification(INotification):
    def __init__(self):
        self.email_service = EmailService()

    def send(self, message: str, recipient: str) -> None:
        self.email_service.send_email(message, recipient)
