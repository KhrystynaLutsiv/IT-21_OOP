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