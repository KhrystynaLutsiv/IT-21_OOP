class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} starts the engine.")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def start_engine(self):
        super().start_engine()
        print("Vroom vroom!")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

car = Car('Toyota', 'Corolla', 2020)
car.start_engine()

print(car)
