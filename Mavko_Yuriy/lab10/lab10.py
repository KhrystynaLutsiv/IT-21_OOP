class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            return "Age cannot be negative"
        self._age = value
    
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age

person = Person("Alice", 25)

print(f"Name: {person.name}")
print(f"Age: {person.age}")
person.age = 30
print(f"Updated Age: {person.age}")
del person.age
