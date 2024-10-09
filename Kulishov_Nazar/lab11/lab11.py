from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass
class Warrior(Character):
    def attack(self):
        return "Воїн атакує мечем!"

class Mage(Character):
    def attack(self):
        return "Маг використовує закляття!"

class Archer(Character):
    def attack(self):
        return "Лучник стріляє з лука!"
class CharacterFactory:
    def create_character(self, character_type):
        if character_type == "Warrior":
            return Warrior()
        elif character_type == "Mage":
            return Mage()
        elif character_type == "Archer":
            return Archer()
        else:
            raise ValueError("Невідомий тип персонажа")
if __name__ == "__main__":
    factory = CharacterFactory()

    # Запитати у гравця, якого персонажа створити
    character_type = input("Виберіть тип персонажа (Warrior, Mage, Archer): ")

    try:
        character = factory.create_character(character_type)
        print(character.attack())
    except ValueError as e:
        print(e)
