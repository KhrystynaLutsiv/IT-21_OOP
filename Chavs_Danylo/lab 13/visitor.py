from abc import ABC, abstractmethod


class ShoppingCartVisitor(ABC):
    @abstractmethod
    def visit_electronics(self, electronics):
        pass

    @abstractmethod
    def visit_clothing(self, clothing):
        pass

    @abstractmethod
    def visit_groceries(self, groceries):
        pass


class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Electronics(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_electronics(self)

class Clothing(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_clothing(self)

class Groceries(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_groceries(self)

class PriceCalculator(ShoppingCartVisitor):
    def visit_electronics(self, electronics):
        discount = 0.10 * electronics.price
        final_price = electronics.price - discount
        print(f"Електроніка, початкова ціна: ${electronics.price}, ціна зі знижкою: ${final_price:.2f}")
        return final_price

    def visit_clothing(self, clothing):
        final_price = clothing.price - 5
        print(f"Одяг, початкова ціна: ${clothing.price}, ціна зі знижкою: ${final_price:.2f}")
        return final_price

    def visit_groceries(self, groceries):
        print(f"Ціна на продукти: ${groceries.price}")
        return groceries.price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self, visitor):
        total = 0
        for item in self.items:
            total += item.accept(visitor)
        return total


cart = ShoppingCart()
cart.add_item(Electronics(100))
cart.add_item(Clothing(50))
cart.add_item(Groceries(20))

calculator = PriceCalculator()
total_price = cart.calculate_total(calculator)
print(f"Загальна ціна після знижок: ${total_price:.2f}")
