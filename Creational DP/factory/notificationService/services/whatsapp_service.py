class WhatsAppService:
    def send_whatsapp_message(self, message: str, recipient: str) -> None:
        print(f"Sending WhatsApp message to {recipient}: {message}")
