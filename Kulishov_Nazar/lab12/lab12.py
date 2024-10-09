from abc import ABC, abstractmethod

# Абстракція
class Menu(ABC):
    @abstractmethod
    def show_items(self):
        pass

# Реалізація (Інтерфейси для елементів меню)
class FoodItem(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

# Конкретні реалізації елементів меню
class Burger(FoodItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Fries(FoodItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Soda(FoodItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

# Конкретна реалізація меню
class FastFoodMenu(Menu):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("Menu:")
        for item in self.items:
            print(f"{item.get_name()}: ${item.get_price():.2f}")

# Використання
if __name__ == "__main__":
    # Створюємо меню
    fast_food_menu = FastFoodMenu()
    fast_food_menu.add_item(Burger("Cheeseburger", 5.99))
    fast_food_menu.add_item(Fries("French Fries", 2.49))
    fast_food_menu.add_item(Soda("Cola", 1.99))

    # Відображаємо меню
    fast_food_menu.show_items()
