from notifications.notification import Notification

class HandlerNotifications:
    def send(self, sender: Notification, message: str) -> None:
        status = sender.send(message)
        if status:
            print("Message sent successfully")
