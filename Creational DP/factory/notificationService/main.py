from notification_manager import NotificationManager

def main():
    recipient = "someone@example.com"

    manager = NotificationManager()

    manager.send_notification("email", "Hello via Email!", recipient)

    sms_recipient = "+1234567890" 
    manager.send_notification("sms", "Hello via SMS!", sms_recipient)

    whatsapp_recipient = "+1234567890" 
    manager.send_notification("whatsapp", "Hello via WhatsApp!", whatsapp_recipient)

if __name__ == "__main__":
    main()
