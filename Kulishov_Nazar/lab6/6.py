class MyClass:
    # Змінна класу для лічильника об'єктів
    objects_created = 0

    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        # Один з атрибутів створюється на основі інших
        self.combined_attribute = arg1 + arg2 + arg3
        # Збільшуємо лічильник об'єктів при створенні нового об'єкта
        MyClass.objects_created += 1

    def generate_description(self):
        # Генеруємо опис об'єкта на основі його властивостей
        return f"MyClass object with attributes: arg1={self.arg1}, arg2={self.arg2}, arg3={self.arg3}, combined_attribute={self.combined_attribute}"

# Створюємо об'єкти на основі класу
obj1 = MyClass(1, 2, 3)
obj2 = MyClass(4, 5, 6)

# Викликаємо метод генерації опису об'єктів
print(obj1.generate_description())
print(obj2.generate_description())

# Використання змінної класу для лічильника
print("Total objects created:", MyClass.objects_created)

