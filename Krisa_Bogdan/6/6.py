class MyClass:
    class_variable = "Це змінна класу"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        return self.instance_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable


my_object = MyClass("Це змінна об'єкта")

print(my_object.instance_method())

print(MyClass.class_method())
