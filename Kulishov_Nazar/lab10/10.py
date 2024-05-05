import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радіус повинен бути додатнім числом")
        self._radius = value

    @property
    def area(self):
        return math.pi * self.radius ** 2

# Приклад використання
circle = Circle(5)
print("Радіус кола:", circle.radius)
print("Площа кола:", circle.area)

# Змінюємо радіус та перевіряємо площу
circle.radius = 7
print("Новий радіус кола:", circle.radius)
print("Нова площа кола:", circle.area)
