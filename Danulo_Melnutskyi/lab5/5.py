class Car:
    wheels = 4

    # Конструктор класу
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} starts the engine.")

my_car = Car('Toyota', 'Corolla')

# Отримання значення властивості
print(my_car.brand)

# Виклик функції об'єкту
my_car.start_engine()
