from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass
class PayPalPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount}  PayPal.")
class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} Credit Card.")
class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount):
        payment_method.process(amount)

if __name__ == "__main__":
    paypal = PayPalPayment()
    credit_card = CreditCardPayment()
    processor = PaymentProcessor()
    processor.process_payment(paypal, 100) 
    processor.process_payment(credit_card, 200) 
    class GooglePayPayment(PaymentMethod):
        def process(self, amount):
            print(f"Processing ${amount}  Google Pay.")

    google_pay = GooglePayPayment()
    processor.process_payment(google_pay, 150)  