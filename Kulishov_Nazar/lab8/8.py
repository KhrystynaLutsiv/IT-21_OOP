# Батьківський клас
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says something.")


# Дочірній клас 1
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")


# Дочірній клас 2
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} meows.")


# Використання методів об'єктів-представників іншого дочірнього класу
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def fly(self):
        print(f"{self.name} flies.")


# Створення об'єктів
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "Tabby")
bird = Bird("Polly", "Parrot")

# Виклик методів
dog.speak()
cat.speak()
bird.fly()

# Перевірка за допомогою isinstance та issubclass
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True
