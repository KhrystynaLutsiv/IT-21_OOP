class Car:
    def drive(self):
        raise NotImplementedError("Цей метод має бути перевизначений у дочірньому класі")

class Sedan(Car):
    def drive(self):
        return "Керування легковим автомобілем"

class Truck(Car):
    def drive(self):
        return "Керування вантажівкою"

class SportsCar(Car):
    def drive(self):
        return "Керування спортивним автомобілем"

class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == 'sedan':
            return Sedan()
        elif car_type == 'truck':
            return Truck()
        elif car_type == 'sportscar':
            return SportsCar()
        else:
            raise ValueError(f"Невідомий тип автомобіля: {car_type}")

factory = CarFactory()

sedan = factory.create_car('sedan')
print(sedan.drive())

truck = factory.create_car('truck')
print(truck.drive())

sports_car = factory.create_car('sportscar')
print(sports_car.drive())

try:
    unknown_car = factory.create_car('motorbike')
except ValueError as e:
    print(e)
