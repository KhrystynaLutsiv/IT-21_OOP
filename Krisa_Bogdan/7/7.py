class MyClass:
    count = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = a + b
        MyClass.count += 1

    def describe(self):
        return f"Об'єкт класу MyClass з a={self.a}, b={self.b} та sum={self.sum}"

    @classmethod
    def get_count(cls):
        return cls.count


obj1 = MyClass(1, 2)
obj2 = MyClass(3, 4)
obj3 = MyClass(5, 6)

print(obj1.describe())
print(obj2.describe())
print(obj3.describe())

print(MyClass.get_count())
