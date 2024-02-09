from notifications.notification import Notification

class AppNotification(Notification):
    def send(self, message) -> bool:
        print(f"Sending {message} to the app")
        return True
