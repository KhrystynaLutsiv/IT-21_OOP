class People:
    count = 0

    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

        self.attr = f"{self.name}-{self.age}-{self.status}"
        People.count += 1

    def print_values(self):
        return f"Object description: name = {self.name}, age = {self.age}, status = {self.status}\n attr = {self.attr}"

obj1 = People("Yuriy", 21, "Student")
obj2 = People("Petro", 32, "Homeless")
obj3 = People("Onufriy", 44, "Priest")

print(obj1.print_values())
print(obj2.print_values())
print(obj3.print_values())

print("Total number of objects created:", People.count)
