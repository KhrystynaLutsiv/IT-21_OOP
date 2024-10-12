from abc import ABC, abstractmethod

# Абстракція для меню
class Menu(ABC):
    def __init__(self, implementer):
        self.implementer = implementer
    @abstractmethod
    def show_items(self):
        pass

# Реалізація елементів меню (реалізація)
class MenuImplementer(ABC):
    @abstractmethod
    def get_items(self):
        pass

# Конкретна реалізація меню фаст-фуду
class FastFoodMenu(Menu):
    def show_items(self):
        print("Fast Food Menu:")
        for item in self.implementer.get_items():
            print(f"{item.get_name()}: ${item.get_price():.2f}")

# Конкретна реалізація елементів фаст-фуду
class FastFoodItems(MenuImplementer):
    def __init__(self):
        self.items = [
            Burger("Cheeseburger", 5.99),
            Fries("French Fries", 2.49),
            Soda("Cola", 1.99)
        ]
    
    def get_items(self):
        return self.items

# Ті ж класи для елементів меню
class Burger:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Fries:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Soda:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

# Використання
if __name__ == "__main__":
    # Створюємо меню з реалізацією елементів
    fast_food_items = FastFoodItems()
    fast_food_menu = FastFoodMenu(fast_food_items)
    fast_food_menu.show_items()
