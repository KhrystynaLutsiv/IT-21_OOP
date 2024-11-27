from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()

# Використання
circle = Circle(5)
square = Square(4)
calculator = AreaCalculator()

print(calculator.calculate_area(circle))  # Площа кола
print(calculator.calculate_area(square))  # Площа квадрата
