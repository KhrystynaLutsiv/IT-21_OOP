class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

    def __del__(self):
        print(f"Deleting {self.brand} {self.model}")

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __format__(self, format_spec):
        return f"{self.brand} {self.model}".__format__(format_spec)


class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

    def drive(self):
        print("Driving the car")

    def __del__(self):
        super().__del__()
        print("Deleting car")

    def __str__(self):
        return f"{super().__str__()}, Color: {self.color}"

    def __format__(self, format_spec):
        return f"{super().__format__(format_spec)}, Color: {self.color}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}")

    def ride(self):
        print("Riding the motorcycle")

    def __del__(self):
        super().__del__()
        print("Deleting motorcycle")

    def __str__(self):
        return f"{super().__str__()}, Type: {self.type}"

    def __format__(self, format_spec):
        return f"{super().__format__(format_spec)}, Type: {self.type}"


car = Car("BMW", "M4", "White")
print(str(car))
print(format(car, "s"))

car.display_info()
car.drive()

print()

motorcycle = Bicycle("Ducati", "Panigale v4", "Sport-bike")
print(str(motorcycle))
print(format(motorcycle, "s"))

motorcycle.display_info()
motorcycle.ride()
