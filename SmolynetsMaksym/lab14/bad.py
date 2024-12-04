class PaymentProcessor:
    @staticmethod
    def process_payment(payment_type, amount):
        if payment_type == "credit_card":
            pass
        elif payment_type == "paypal":
            pass
        else:
            raise ValueError("Unknown payment type")
