class ParentClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, {self.name}!"

class ChildClass1(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        return f"{super().greet()} Мені {self.age} років."

class ChildClass2(ParentClass):
    def interact_with_other(self, other):
        return f"{self.name} каже: '{other.greet()}'"

child1 = ChildClass1("Child1", 10)
child2 = ChildClass2("Child2")

print(child2.interact_with_other(child1))