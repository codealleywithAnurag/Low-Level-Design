from notification_factory import NotificationFactory

class NotificationManager:
    def __init__(self):
        self.factory = NotificationFactory()

    def send_notification(self, notification_type: str, message: str, recipient: str) -> None:
        try:
            notification = self.factory.get_notification(notification_type)
            notification.send(message, recipient)
        except ValueError as e:
            print(e)
