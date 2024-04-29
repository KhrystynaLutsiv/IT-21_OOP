class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

class CustomVehicle(Vehicle):
    def custom_function(self):
        return "This is a custom function for CustomVehicle class."

car1 = CustomVehicle()
car1.name = "Fer"
car1.kind = "sportcar"
car1.color = "red"
car1.value = 77777777
print(car1.description())
print(car1.custom_function())

car2 = CustomVehicle()
car2.name = "BMW"
car2.kind = "SUV"
car2.color = "blue"
car2.value = 888888888
print(car2.description())
print(car2.custom_function())
