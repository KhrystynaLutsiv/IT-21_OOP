class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print("Ім'я видалено.")
        del self._name

person = Person("Максим")
print(person.name)  

person.name = "Артурчик"  
print(person.name)  

del person.name  

