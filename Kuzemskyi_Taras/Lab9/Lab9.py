class Automobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("The automobile is starting.")

    def stop(self):
        print("The automobile is stopping.")

    def honk(self):
        print("Beep beep!")


class Car(Automobile):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def start(self):
        print("The car is starting.")

    def stop(self):
        print("The car is stopping.")


class Truck(Automobile):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def start(self):
        print("The truck is starting.")

    def stop(self):
        print("The truck is stopping.")

    def honk(self):
        print("HOOOONK!")


# Приклад використання:

car = Car("Toyota", "Corolla", 4)
truck = Truck("Volvo", "FH16", "40 tons")

car.start()   # Виведе: The car is starting.
truck.start() # Виведе: The truck is starting.

car.stop()    # Виведе: The car is stopping.
truck.stop()  # Виведе: The truck is stopping.

car.honk()    # Виведе: Beep beep!
truck.honk()  # Виведе: HOOOONK!
