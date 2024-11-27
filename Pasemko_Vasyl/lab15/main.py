"""
# Приклад "брудного" коду без дотримання принципів SOLID
class BadShape:
    def __init__(self, type_shape, size1, size2=None):
        self.type = type_shape  # 'circle' або 'rectangle'
        self.size1 = size1      # width для rectangle, radius для circle
        self.size2 = size2      # height для rectangle
    
    def calculate_area(self):
        if self.type == 'rectangle':
            return self.size1 * self.size2
        elif self.type == 'circle':
            return 3.14 * self.size1 * self.size1
        else:
            raise ValueError("Невідомий тип фігури")

class BadCalculator:
    def calculate_and_print(self, shapes):
        total = 0
        for shape in shapes:
            area = shape.calculate_area()
            print(f"Площа фігури: {area}")
            total += area
        print(f"Загальна площа: {total}")
        return total

# Використання "брудного" коду
shapes = [
    BadShape('rectangle', 5, 4),
    BadShape('circle', 3)
]
calc = BadCalculator()
calc.calculate_and_print(shapes)
"""

# Покращена версія коду з дотриманням SOLID принципів
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_total_area(self, shapes):
        return sum(shape.area() for shape in shapes)

def main():
    shapes = [Rectangle(5, 4), Circle(3)]
    calculator = AreaCalculator()
    total_area = calculator.calculate_total_area(shapes)
    print(f"Загальна площа: {total_area}")

if __name__ == "__main__":
    main()