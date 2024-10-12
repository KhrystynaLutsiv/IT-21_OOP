import copy

class Address:
    def __init__(self, city, street, house_number):
        self.city = city
        self.street = street
        self.house_number = house_number

    def __str__(self):
        return f"{self.street} {self.house_number}, {self.city}"

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

address = Address("Malehiv", "Shevchenka", 66)
person = Person("Dima Antonyuk", 18, address)

person_clone = person.clone()

person_clone.name = "Anton Dmytruk"
person_clone.address.city = "Dubliany"

print("Original Person:")
print(person)

print("\nCloned Person:")
print(person_clone)

print(f"\nOriginal is clone: {person is person_clone}")
print(f"Original address is clone address: {person.address is person_clone.address}")
