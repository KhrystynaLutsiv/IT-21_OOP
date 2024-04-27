class Car:
    total_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        # Один з атрибутів створюється на основі інших
        self.description = f"{self.brand} {self.model} ({self.year})"
        # 5. Лічильник створених об'єктів
        Car.total_cars += 1

    def get_description(self):
        return self.description

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

car1 = Car('Toyota', 'Corolla', 2020)
car2 = Car('Honda', 'Civic', 2021)

# Виклик методу за допомогою об'єкта
print(car1.get_description())
print(car2.get_description())

# Виклик методу за допомогою класу
print(Car.get_total_cars())
