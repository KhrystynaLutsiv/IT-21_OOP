class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Це тварина розмовляє"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Гав"

class Cat(Animal):
    def speak(self):
        return "Мяу"

    def interact(self, dog):
        print(f"{self.name} (кіт) і {dog.name} (собака) граються разом")

dog = Dog("Рекс", "Бульдог")
cat = Cat("Мурка")

print(isinstance(dog, Animal))
print(isinstance(cat, Animal))

print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))

cat.interact(dog)