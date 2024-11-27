from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


shapes = [
        Rectangle(width=4, height=5),
        Circle(radius=3)
    ]

total_area = 0
for shape in shapes:
    total_area += shape.calculate_area()

print(f"Загальна площа: {total_area}")
