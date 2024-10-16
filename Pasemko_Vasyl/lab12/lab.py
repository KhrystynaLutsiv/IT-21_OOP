class Coffee:
    def cost(self):
        return 5  # Базова вартість кави

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2  # Додаємо вартість молока

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  # Додаємо вартість цукру

# Використання
simple_coffee = Coffee()
print(f"Simple coffee cost: ${simple_coffee.cost()}")  # Виведе 5

milk_coffee = MilkDecorator(simple_coffee)
print(f"Coffee with milk cost: ${milk_coffee.cost()}")  # Виведе 7

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Coffee with milk and sugar cost: ${sugar_milk_coffee.cost()}")  # Виведе 8
