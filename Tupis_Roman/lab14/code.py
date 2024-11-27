#поганий приклад
class OrderManager:
    def create_order(self, data):
        # Логіка створення замовлення
        pass

    def send_confirmation_email(self, order):
        # Логіка відправлення електронного листа
        pass

    def log_order(self, order):
        # Логіка журналювання замовлення
        pass



#приклад згідно SRP

class OrderCreator:
    def create_order(self, data):
        # Логіка створення замовлення
        pass

class EmailService:
    def send_confirmation_email(self, order):
        # Логіка відправлення електронного листа
        pass

class Logger:
    def log_order(self, order):
        # Логіка журналювання замовлення
        pass


