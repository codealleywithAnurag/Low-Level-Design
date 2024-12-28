class EmailService:
    def send_email(self, message: str, recipient: str) -> None:
        print(f"Sending Email to {recipient}: {message}")
