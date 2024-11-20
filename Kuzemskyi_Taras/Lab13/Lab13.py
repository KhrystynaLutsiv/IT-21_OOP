class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Цей метод має бути перевизначений у дочірньому класі")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} за допомогою кредитної картки."

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} за допомогою PayPal."

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} за допомогою криптовалюти."

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, item):
        self.items.append(item)

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self):
        total_amount = sum(item['price'] for item in self.items)
        if self.payment_strategy is None:
            return "Метод оплати не вибрано."
        return self.payment_strategy.pay(total_amount)

if __name__ == "__main__":
    cart = ShoppingCart()
    
    cart.add_item({'name': 'Книга', 'price': 200})
    cart.add_item({'name': 'Ручка', 'price': 50})

    cart.set_payment_strategy(CreditCardPayment())
    print(cart.checkout())

    cart.set_payment_strategy(PayPalPayment())
    print(cart.checkout()) 

    cart.set_payment_strategy(CryptoPayment())
    print(cart.checkout())
