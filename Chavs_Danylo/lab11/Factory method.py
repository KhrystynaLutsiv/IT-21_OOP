class Vehicle:
    def __init__(self, wheels, engine_type, color):
        self.wheels = wheels
        self.engine_type = engine_type
        self.color = color

    def __str__(self):
        return f"Транспортний засіб з {self.wheels} колесами, {self.engine_type} двигуном та кольором {self.color}"


class VehicleFactory:
    def create_vehicle(self):
        raise NotImplementedError("Підкласи повинні реалізувати цей метод")


class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Vehicle(4, "Бензиновий", "Червоний")


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Vehicle(2, "Бензиновий", "Чорний")


class ElectricCarFactory(VehicleFactory):
    def create_vehicle(self):
        return Vehicle(4, "Електричний", "Синій")


def build_vehicle(factory: VehicleFactory):
    return factory.create_vehicle()



car_factory = CarFactory()
motorcycle_factory = MotorcycleFactory()
electric_car_factory = ElectricCarFactory()


car = build_vehicle(car_factory)
motorcycle = build_vehicle(motorcycle_factory)
electric_car = build_vehicle(electric_car_factory)


print(car)
print(motorcycle)
print(electric_car)
