from notifications.i_notification import INotification
from services.whatsapp_service import WhatsAppService

class WhatsAppNotification(INotification):
    def __init__(self):
        self.whatsapp_service = WhatsAppService()

    def send(self, message: str, recipient: str) -> None:
        self.whatsapp_service.send_whatsapp_message(message, recipient)
