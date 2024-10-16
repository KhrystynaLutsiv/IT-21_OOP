class Government:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Створюємо новий уряд.")
            cls._instance = super(Government, cls).__new__(cls)
        else:
            print("Уряд вже існує.")
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name

goverment1 = Government("Уряд України")
print(goverment1.name)

goverment2 = Government("Новий Уряд")
print(goverment2.name)

print(goverment1 is goverment2)
