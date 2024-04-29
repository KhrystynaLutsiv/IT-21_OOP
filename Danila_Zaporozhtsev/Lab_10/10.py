class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}, area={self.area}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Rectangle object is deleted")

# Створюємо об'єкт Rectangle
rect = Rectangle(5, 4)

# Використання getter'ів
print(rect.width)  # 5
print(rect.height)  # 4
print(rect.area)  # 20

# Використання setter'ів
rect.width = 6
rect.height = 8
print(rect.width)  # 6
print(rect.height)  # 8
print(rect.area)  # 48

# Видалення об'єкту
del rect  # Виведе "Rectangle object is deleted"
