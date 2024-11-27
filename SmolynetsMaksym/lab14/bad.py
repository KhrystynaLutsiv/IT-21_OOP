class PaymentProcessor:
    @staticmethod
    def process_payment(payment_type, amount):
        if payment_type == "credit_card":
            # Обробка платежу через кредитну картку
            pass
        elif payment_type == "paypal":
            # Обробка платежу через PayPal
            pass
        else:
            raise ValueError("Unknown payment type")
