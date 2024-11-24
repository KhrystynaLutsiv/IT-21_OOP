class Order:
    def __init__(self, items, customer_type):
        self.items = items  # список предметів із цінами
        self.customer_type = customer_type  # тип клієнта ("regular", "premium", "vip")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]

        # Знижки залежно від типу клієнта
        if self.customer_type == "regular":
            total *= 1
        elif self.customer_type == "premium":
            total *= 0.9
        elif self.customer_type == "vip":
            total *= 0.8

        return total

    def print_invoice(self):
        print("Invoice")
        print("--------")
        for item in self.items:
            print(f"{item['name']} x{item['quantity']}: {item['price'] * item['quantity']}")
        print("--------")
        print(f"Total: {self.calculate_total()}")
class DiscountStrategy:
    """Абстрактний клас для стратегій знижок"""
    def apply_discount(self, total):
        return total

class RegularCustomerDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total

class PremiumCustomerDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total * 0.9

class VIPCustomerDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total * 0.8

class Order:
    def __init__(self, items, discount_strategy: DiscountStrategy):
        self.items = items  # список предметів із цінами
        self.discount_strategy = discount_strategy

    def calculate_total(self):
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return self.discount_strategy.apply_discount(total)

class InvoicePrinter:
    """Клас для друку рахунку"""
    @staticmethod
    def print_invoice(order: Order):
        print("Invoice")
        print("--------")
        for item in order.items:
            print(f"{item['name']} x{item['quantity']}: {item['price'] * item['quantity']}")
        print("--------")
        print(f"Total: {order.calculate_total()}")
# Товари в замовленні
items = [
    {"name": "Laptop", "price": 1000, "quantity": 1},
    {"name": "Mouse", "price": 50, "quantity": 2},
]

# Замовлення для VIP-клієнта
discount_strategy = VIPCustomerDiscount()
order = Order(items, discount_strategy)

# Друк рахунку
InvoicePrinter.print_invoice(order)
