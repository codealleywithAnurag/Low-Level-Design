from notifications.email_notification import EmailNotification
from notifications.sms_notification import SMSNotification
from notifications.whatsapp_notification import WhatsAppNotification

class NotificationFactory:
    @staticmethod
    def get_notification(notification_type: str):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "whatsapp":
            return WhatsAppNotification()
        else:
            raise ValueError(f"Unsupported notification type: {notification_type}")
