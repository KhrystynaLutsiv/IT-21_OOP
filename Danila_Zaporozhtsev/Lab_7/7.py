# Використання клас иетоду

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print("Кількість створених об'єктів:", Counter.get_count())

# Приклад використання статичних методів
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

print("Додавання:", Calculator.add(5, 3))
print("Віднімання:", Calculator.subtract(10, 4))


