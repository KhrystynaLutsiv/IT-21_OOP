from abc import ABC, abstractmethod

class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, order: Order):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, order: Order):
        print(f"Processing credit card payment for Order ID: {order.order_id}, Amount: {order.amount}")


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, order: Order):
        print(f"Processing PayPal payment for Order ID: {order.order_id}, Amount: {order.amount}")

class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_order(self, order: Order):
        # Обробка замовлення через переданий платіжний процесор
        self.payment_processor.process_payment(order)

order = Order(order_id=1, amount=100)

credit_card_processor = CreditCardPaymentProcessor()
paypal_processor = PayPalPaymentProcessor()

order_processor_credit = OrderProcessor(credit_card_processor)
order_processor_paypal = OrderProcessor(paypal_processor)

order_processor_credit.process_order(order)  
order_processor_paypal.process_order(order)   

