from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        # Обробка платежу через кредитну картку
        pass


class PayPalPayment(PaymentMethod):
    def process(self, amount):
        # Обробка платежу через PayPal
        pass


class PaymentProcessor:
    @staticmethod
    def process_payment(payment_method: PaymentMethod, amount):
        payment_method.process(amount)