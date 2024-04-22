class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Юра", 17)

print(f"Вид: {person1.species}")

person1.age = 18

print(f"Вік: {person1.age}")
