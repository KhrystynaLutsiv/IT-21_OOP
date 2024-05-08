class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Підклас повинен реалізувати цей метод")

    def __str__(self):
        return self.name


class Dog(Animal):
    def speak(self):
        return "Гав"


class Cat(Animal):
    def speak(self):
        return "Мяу"


def animal_speak(animal):
    print(animal.speak())


dog = Dog("Рекс")
cat = Cat("Мурка")

animal_speak(dog)
animal_speak(cat)

print(dog)
print(cat)
