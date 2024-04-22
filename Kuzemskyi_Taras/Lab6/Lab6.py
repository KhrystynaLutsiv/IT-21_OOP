class Student:
    # Змінна класу для лічильника
    count = 0

    def __init__(self, name, surname, faculty, course):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.course = course
        # Атрибут, створений на основі інших атрибутів
        self.full_name = f"{name} {surname}"
        # Збільшуємо лічильник при створенні нового об'єкта
        Student.count += 1

    def generate_description(self):
        return f"Name: {self.name}, Surname: {self.surname}, Faculty: {self.faculty}, Course: {self.course}, Full Name: {self.full_name}"

# Створюємо об'єкти на основі класу
student1 = Student("Stepan", "Kravets", "Computer Science", 3)
student2 = Student("Ivan", "Koval", "Mathematics", 2)

# Викликаємо метод generate_description() для об'єктів
print("Description of student1:", student1.generate_description())
print("Description of student2:", student2.generate_description())

# Використовуємо змінну класу для виведення лічильника
print("Total number of students:", Student.count)
