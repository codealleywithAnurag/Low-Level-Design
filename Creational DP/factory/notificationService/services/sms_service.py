class SMSService:
    def send_sms(self, message: str, recipient: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")
