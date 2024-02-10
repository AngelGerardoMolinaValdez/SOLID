from notifications.notification import Notification

class EmailNotification(Notification):
    def __init__(self, email: str) -> None:
        self.email = email

    def send(self, message: str) -> bool:
        print("EmailNotification: " + message + " to " + self.email + ".")
        return True
