class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def some_business_logic(self):
        return "Виконання бізнес-логіки"


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)
print(singleton1.some_business_logic())
