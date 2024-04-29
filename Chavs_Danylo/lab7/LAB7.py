class MyClass:
    class_variable = 0  
    
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.calc_attr = arg1 + arg2  
        MyClass.class_variable += 1  

    def generate_description(self):
        return f"Object properties: arg1={self.arg1}, arg2={self.arg2}"

    @classmethod
    def from_string(cls, string):
        args = map(int, string.split(','))
        return cls(*args)
    
    @classmethod
    def print_class_variable(cls):
        print(f"Class variable: {cls.class_variable}")

    @staticmethod
    def add(x, y):
        return x + y


obj1 = MyClass(10, 20)
obj2 = MyClass(30, 40)

print(obj1.calc_attr)  
print(obj1.generate_description())  
print(obj2.generate_description())  

print(MyClass.class_variable)  

obj3 = MyClass.from_string('50, 60')
print(obj3.generate_description())

MyClass.print_class_variable()

print(MyClass.add(10, 20))
