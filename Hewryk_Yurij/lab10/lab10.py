class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Ім'я повинно бути рядком")
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Вік повинен бути цілим числом")
        self._age = value

    @age.deleter
    def age(self):
        del self._age

person = Person("Іван", 30)

print(person.name)
print(person.age)

person.name = "Петро"
person.age = 35

print(person.name)
print(person.age)

del person.name
del person.age
