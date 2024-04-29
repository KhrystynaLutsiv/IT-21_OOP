class MyClass:
    class_variable = 0  
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.calc_attr = arg1 + arg2  
        MyClass.class_variable += 1  
    def generate_description(self):
        return f"Object properties: arg1={self.arg1}, arg2={self.arg2}"


obj1 = MyClass(10, 20)
obj2 = MyClass(30, 40)

print(obj1.calc_attr)  
print(obj1.generate_description())  
print(obj2.generate_description())  

print(MyClass.class_variable)  