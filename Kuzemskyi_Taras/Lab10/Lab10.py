class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

# Створення об'єкта
circle = Circle(5)

# Виклик методу diameter як атрибута, без застосування дужок
print(circle.diameter)  # Виведе 10

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter
    @property
    def width(self):
        return self._width

    # Setter
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be a positive number")

    # Delete
    @width.deleter
    def width(self):
        del self._width

# Створення об'єкта
rect = Rectangle(5, 6)

# Виклик getter'а
print(rect.width)  # Виведе 5

# Виклик setter'а
rect.width = 10
print(rect.width)  # Виведе 10

# Виклик delete'ра
del rect.width
#print(rect.width)  # Викличе помилку, бо атрибут був видалений
