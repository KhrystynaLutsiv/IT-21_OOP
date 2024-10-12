import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

# Створюємо об'єкт-прототип
original_prototype = ConcretePrototype(value=10)

# Клонуємо об'єкт
clone1 = original_prototype.clone()
clone2 = original_prototype.clone()

print(f"Original value: {original_prototype.value}")  # Виведе 10
print(f"Clone 1 value: {clone1.value}")  # Також виведе 10
print(f"Clone 2 value: {clone2.value}")  # Також виведе 10
