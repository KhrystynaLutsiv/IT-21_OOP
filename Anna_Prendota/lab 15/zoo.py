class Zoo:
    def __init__(self):
        # Зберігання тварин у словнику за типом
        self.animals = {
            "lion": [],
            "elephant": [],
            "monkey": []
        }

    def add_animal(self, animal_type, name):
        """Додає тварину до відповідного списку за типом."""
        if animal_type not in self.animals:
            print(f"Помилка: тип '{animal_type}' не підтримується.")
            return

        if isinstance(name, str):
            self.animals[animal_type].append(name)
            print(f"{animal_type.capitalize()} {name} доданий до зоопарку.")
        else:
            print("Помилка: ім'я повинне бути рядком.")

    def show_all_animals(self):
        """Показує всіх тварин у зоопарку за типом."""
        if not any(self.animals.values()):
            print("Зоопарк порожній.")
        else:
            print("У нашому зоопарку живуть:")
            for animal_type, names in self.animals.items():
                if names:
                    print(f"{animal_type.capitalize()}s: {', '.join(names)}")

    def make_sounds(self):
        """Заставляє тварин видавати звуки за типом."""
        sounds = {
            "lion": "Рррр! Я Лев.",
            "elephant": "Трууу! Я Слон.",
            "monkey": "Ууу! Я Мавпа."
        }

        if not any(self.animals.values()):
            print("Немає тварин для видачі звуків.")
        else:
            print("Тварини в зоопарку видають звуки:")
            for animal_type, names in self.animals.items():
                if names:
                    for name in names:
                        print(f"{name} ({animal_type.capitalize()}): {sounds[animal_type]}")
                        

# Створення зоопарку та додавання тварин
zoo = Zoo()
zoo.add_animal("lion", "Сімба")
zoo.add_animal("elephant", "Дамбо")
zoo.add_animal("monkey", "Джек")
zoo.add_animal("tiger", "Шерхан")  # Тип тварини не підтримується

# Відображення всіх тварин у зоопарку
zoo.show_all_animals()

# Видача звуків тваринами
zoo.make_sounds()
