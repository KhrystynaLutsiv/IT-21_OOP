
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} starts the engine.")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        # Використання методу super
        super().__init__(brand, model)
        self.year = year

    def honk_horn(self):
        print("Beep beep!")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def rev_engine(self):
        print("Vroom vroom!")

car = Car('Toyota', 'Corolla', 2020)
motorcycle = Motorcycle('Honda', 'CBR600RR', 2021)

vehicles = [car, motorcycle]
for vehicle in vehicles:
    vehicle.start_engine()

print(isinstance(car, Vehicle))  # повертає True
print(issubclass(Car, Vehicle))  # повертає True
