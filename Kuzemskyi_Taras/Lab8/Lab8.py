# Створення батьківського класу
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return "Driving"

# Створення дочірніх класів і методів super    
class PassengerCar(Car):
    def __init__(self, brand, model, num_seats):
        super().__init__(brand, model)
        self.num_seats = num_seats

    def carry_passengers(self):
        return f"Carrying passengers in a {self.brand} {self.model}"

class Truck(Car):
    def __init__(self, brand, model, max_load):
        super().__init__(brand, model)
        self.max_load = max_load

    def carry_cargo(self):
        return f"Carrying cargo in a {self.brand} {self.model}"

# Використання методів об'єктів-представників іншого дочірнього класу   
passenger_car = PassengerCar("Toyota", "Camry", 5)
truck = Truck("Ford", "F-150", 2000)

if isinstance(passenger_car, Truck):
    print(passenger_car.carry_cargo())
else:
    print(truck.carry_cargo())

car = Car("Toyota", "Corolla")
passenger_car = PassengerCar("Toyota", "Camry", 5)
truck = Truck("Ford", "F-150", 2000)

# Перевірка чи є об'єкт екземпляром певного класу
print(isinstance(car, Car))  # True
print(isinstance(passenger_car, PassengerCar))  # True
print(isinstance(truck, Truck))  # True

# Перевірка чи клас є підкласом іншого класу
print(issubclass(PassengerCar, Car))  # True
print(issubclass(Truck, Car))  # True
print(issubclass(PassengerCar, Truck))  # False
