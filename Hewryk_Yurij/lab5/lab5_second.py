class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Двигун запущено!")

    def drive(self):
        print("Автомобіль їде!")

car = Car("Toyota", "Camry", 2023)

car.start_engine()
car.drive()
