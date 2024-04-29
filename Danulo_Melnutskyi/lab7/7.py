class Car:
    total_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        # Збільшення лічильника автомобілів
        Car.total_cars += 1

    def start_engine(self):
        print(f"{self.brand} {self.model} starts the engine.")

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    @classmethod
    def from_string(cls, car_string):
        brand, model, year = car_string.split('-')
        return cls(brand, model, int(year))

    @staticmethod
    def is_vintage(year):
        return year < 1990

car1 = Car.from_string('Toyota-Corolla-1985')

# Виклик методу класу
print(Car.get_total_cars())

# Виклик статичного методу
print(Car.is_vintage(1985))
