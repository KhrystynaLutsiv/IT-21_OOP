class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Ім'я має бути рядком.")
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
            raise TypeError("Вік має бути цілим числом.")
        self._age = value

    @age.deleter
    def age(self):
        del self._age


student = Student("Іван", 20)

print(student.name)
print(student.age)

student.name = "Петро"
student.age = 21
print(student.name)
print(student.age)

del student.name
del student.age
