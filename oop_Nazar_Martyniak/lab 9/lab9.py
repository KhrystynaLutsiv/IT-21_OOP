class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Підклас повинен реалізувати цей метод")

class Dog(Animal):
    def speak(self):
        return f"{self.name} каже гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} каже м'яу!"

        __str__
    def __str__(self):
        return f"Це кіт з ім'ям {self.name}."

dog = Dog("Рекс")
cat = Cat("Мурка")

print(dog.speak())
print(cat.speak())

print(cat)