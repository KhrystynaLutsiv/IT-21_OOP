class MyClass:
    class_variable = "Я змінна класу"

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, {self.name}!"

object1 = MyClass("Object1")
object2 = MyClass("Object2")

print(object1.greet())
print(object2.greet())

print(MyClass.class_variable)
