
def process_order(order):
    calculate_total(order)
    print_receipt(order)

def calculate_total(order):
    # Логіка підрахунку
    pass

def print_receipt(order):
 
    pass


def get_discount():
    return 5

total = 100
price = total - get_discount()

price = total - 5


def calc(x):
    return x * 10

def calculate_discount(price):
    return price * 10

class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

class Payment:
    def __init__(self, payment_id, amount):
        self.payment_id = payment_id
        self.amount = amount
def apply_discount(price):
    return price * 0.9

def calculate_final_price(price):
    return apply_discount(price)
class Order:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

user = {"is_admin": True}
if user["is_admin"]:
    access = True
else:
    access = False


access = user["is_admin"]

class PaymentMethod:
    def process(self):
        raise NotImplementedError

class PayPalPayment(PaymentMethod):
    def process(self):
        print("Processing PayPal payment")

class CreditCardPayment(PaymentMethod):
    def process(self):
        print("Processing credit card payment")

def process_payment(payment_method: PaymentMethod):
    payment_method.process()

paypal = PayPalPayment()
credit_card = CreditCardPayment()

process_payment(paypal)
process_payment(credit_card)

def process_transaction(order):
    validate_order(order)
    charge_payment(order)
    send_confirmation(order)

def validate_order(order):
    # Перевірка замовлення
    pass

def charge_payment(order):
    # Списання коштів
    pass

def send_confirmation(order):
    # Надсилання підтвердження
    pass
