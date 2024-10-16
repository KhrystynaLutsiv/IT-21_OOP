# Базовий клас для всіх типів автомобілів
class Car:
    def drive(self):
        raise NotImplementedError("Цей метод має бути перевизначений у дочірньому класі")

# Легковий автомобіль (Sedan)
class Sedan(Car):
    def drive(self):
        return "Керування легковим автомобілем"

# Вантажівка (Truck)
class Truck(Car):
    def drive(self):
        return "Керування вантажівкою"

# Спортивний автомобіль (SportsCar)
class SportsCar(Car):
    def drive(self):
        return "Керування спортивним автомобілем"

# Фабрика для створення об'єктів автомобілів
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

# Використання фабрики
factory = CarFactory()

# Створення легкового автомобіля
sedan = factory.create_car('sedan')
print(sedan.drive())  # Виведе: Керування легковим автомобілем

# Створення вантажівки
truck = factory.create_car('truck')
print(truck.drive())  # Виведе: Керування вантажівкою

# Створення спортивного автомобіля
sports_car = factory.create_car('sportscar')
print(sports_car.drive())  # Виведе: Керування спортивним автомобілем

# Спроба створити автомобіль невідомого типу
try:
    unknown_car = factory.create_car('motorbike')
except ValueError as e:
    print(e)  # Виведе: Невідомий тип автомобіля: motorbike
