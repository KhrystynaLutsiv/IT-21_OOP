class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

    def drive(self):
        print("Driving the car")


class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}")

    def ride(self):
        print("Riding the bicycle")


car = Car("BMW", "M8", "black")
car.display_info() 
car.drive()  

print()

bicycle = Bicycle("Giant", "Escape", "Mountain")
bicycle.display_info()  
bicycle.ride()  

