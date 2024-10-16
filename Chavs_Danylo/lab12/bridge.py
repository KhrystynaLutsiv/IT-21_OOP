class NotificationImplementation:
    def send_notification(self, message):
        pass

class EmailNotification(NotificationImplementation):
    def send_notification(self, message):
        print(f"Відправка сповіщення електронною поштою: {message}")

class SMSNotification(NotificationImplementation):
    def send_notification(self, message):
        print(f"Відправка SMS сповіщення: {message}")

class NotificationBridge:
    def __init__(self, implementation):
        self.implementation = implementation

    def notify(self, message):
        self.implementation.send_notification(message)

def client_code(notification):
    notification.notify("У вас нове повідомлення!")

email_notification = EmailNotification()
sms_notification = SMSNotification()

bridge_with_email_notification = NotificationBridge(email_notification)
bridge_with_sms_notification = NotificationBridge(sms_notification)

client_code(bridge_with_email_notification)  
client_code(bridge_with_sms_notification)  
