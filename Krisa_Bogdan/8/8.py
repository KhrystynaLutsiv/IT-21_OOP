class MyClass:
    class_variable = "Це змінна класу"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        return self.instance_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable

    @classmethod
    def alternative_constructor(cls, string):
        return cls(int(string))

    @staticmethod
    def static_method():
        return "Це статичний метод"

obj1 = MyClass(10)
print(obj1.instance_method())

obj2 = MyClass.alternative_constructor("20")
print(obj2.instance_method())

print(MyClass.class_method())

print(MyClass.static_method())
