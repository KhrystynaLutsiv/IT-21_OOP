class PayrollCalculator:    # Порушення OCP
    def calculate_salary(self, employee_type, hours_worked):
        if employee_type == "full_time":
            return hours_worked * 20
        elif employee_type == "contractor":
            return hours_worked * 15
        else:
            raise ValueError("Unknown employee type")



# Дотримання OCP:
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self, hours_worked):
        pass

#постійний співробітник
class FullTimeEmployee(Employee):
    def calculate_salary(self, hours_worked):
        return hours_worked * 20

#підрядник
class Contractor(Employee):
    def calculate_salary(self, hours_worked):
        return hours_worked * 15

#стажер
class Intern(Employee):
    def calculate_salary(self, hours_worked):
        return hours_worked * 10

#клас розрахунку зарплати
class PayrollCalculator:
    def calculate_salary(self, employee: Employee, hours_worked):
        return employee.calculate_salary(hours_worked)

full_time = FullTimeEmployee()
contractor = Contractor()
intern = Intern()

calculator = PayrollCalculator()

print("Full-time salary:", calculator.calculate_salary(full_time, 40))
print("Contractor salary:", calculator.calculate_salary(contractor, 40))
print("Intern salary:", calculator.calculate_salary(intern, 40))
