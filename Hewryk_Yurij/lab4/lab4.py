class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Точка ({self.x}, {self.y})"

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

point1 = Point(1, 2)
point2 = Point(5, 7)
rectangle = Rectangle(point1, point2)

print(f"Площа прямокутника: {rectangle.area()}")
print(f"Інформація про першу точку: {point1}")
print(f"Інформація про другу точку: {point2}")
