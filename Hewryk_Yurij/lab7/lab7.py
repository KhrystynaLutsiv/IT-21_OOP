class MyClass:
    class_variable = "Я змінна класу"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_class_variable(cls, new_value):
        cls.class_variable = new_value

    @classmethod
    def from_string(cls, name_str):
        return cls(name_str)

    @staticmethod
    def static_method():
        return "Це статичний метод!"

object1 = MyClass.from_string("Object1")

MyClass.change_class_variable("Нове значення змінної класу")

print(MyClass.class_variable)

print(MyClass.static_method())