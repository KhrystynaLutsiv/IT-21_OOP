class Student:
    def __init__(self, name, surname, faculty, course):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.course = course

    @classmethod
    def from_string(cls, student_string):
        name, surname, faculty, course = student_string.split(',')
        return cls(name, surname, faculty, int(course))

# Використання альтернативного конструктора
student = Student.from_string("Stepan,Kravets,Computer Science,3")
print(student.name, student.surname, student.faculty, student.course)

class Student1:
    students_count = 0

    def __init__(self, name, surname, faculty, course):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.course = course
        Student1.students_count += 1

    @classmethod
    def get_students_count(cls):
        return cls.students_count

# Використання методу класу
print(Student1.get_students_count())

class Student2:
    @staticmethod
    def greet():
        return "Hello, I am a student!"

# Використання статичного методу
print(Student2.greet())


