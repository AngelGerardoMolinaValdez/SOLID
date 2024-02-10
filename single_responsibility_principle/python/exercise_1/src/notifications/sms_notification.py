from notifications.notification import Notification

class SMSNotification(Notification):
    def __init__(self, phone_number: int) -> None:
        self.phone_number = phone_number

    def send(self, message) -> bool:
        print(f"Sending SMS: {message} to {self.phone_number}.")
        return True
