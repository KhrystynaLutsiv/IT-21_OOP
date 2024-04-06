class MyClass:
    objects_created = 0

    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.combined_attribute = arg1 + arg2 + arg3
        MyClass.objects_created += 1

    @classmethod
    def from_string(cls, string):
        args = string.split(",")
        return cls(*args)

    @classmethod
    def class_method(cls):
        print("Objects created:", cls.objects_created)


# Використання альтернативного конструктора
obj3 = MyClass.from_string("7,8,9")
print(obj3.combined_attribute)

# Виклик методу класу
MyClass.class_method()
