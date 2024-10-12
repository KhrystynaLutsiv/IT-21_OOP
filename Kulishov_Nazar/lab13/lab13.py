from abc import ABC, abstractmethod

# Інтерфейс для стану собаки
class DogState(ABC):
    @abstractmethod
    def behave(self):
        pass

# Конкретний стан: Голодна собака
class HungryState(DogState):
    def behave(self):
        return "Собака голодна. Час годувати!"

# Конкретний стан: Грайлива собака
class PlayfulState(DogState):
    def behave(self):
        return "Собака грайлива. Граємо з м'ячем!"

# Конкретний стан: Втомлена собака
class TiredState(DogState):
    def behave(self):
        return "Собака втомлена. Час відпочити."

# Клас собаки
class Dog:
    def __init__(self):
        self.state = HungryState()  # Початковий стан

    def set_state(self, state: DogState):
        self.state = state

    def act(self):
        print(self.state.behave())

# Використання
if __name__ == "__main__":
    dog = Dog()

    # Собака голодна
    dog.act()

    # Зміна стану на грайливу
    dog.set_state(PlayfulState())
    dog.act()

    # Зміна стану на втомлену
    dog.set_state(TiredState())
    dog.act()
