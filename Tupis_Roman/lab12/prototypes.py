"""Prototype (Прототип)
Для чого він використовується? Патерн Prototype дозволяє створювати нові об’єкти, використовуючи існуючий об’єкт як прототип. Це дозволяє уникнути повторного створення об’єктів з нуля. Наприклад, якщо у нас є об’єкт з певним станом або конфігурацією, ми можемо клонувати його, змінюючи лише необхідні параметри.
"""

import copy

class Animal:
    def __init__(self, species):
        self.species = species

    def clone(self):
        return copy.deepcopy(self)

# Створюємо прототип
original_dog = Animal(species="Dog")

# Клонуємо прототип для створення нових об'єктів
dog1 = original_dog.clone()
dog2 = original_dog.clone()

# Змінюємо властивості клонованих об'єктів
dog1.species = "Golden Retriever"
dog2.species = "Dachshund"

print(f"Dog 1 species: {dog1.species}")
print(f"Dog 2 species: {dog2.species}")

