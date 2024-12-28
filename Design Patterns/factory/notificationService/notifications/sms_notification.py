from notifications.i_notification import INotification
from services.sms_service import SMSService

class SMSNotification(INotification):
    def __init__(self):
        self.sms_service = SMSService()

    def send(self, message: str, recipient: str) -> None:
        self.sms_service.send_sms(message, recipient)
