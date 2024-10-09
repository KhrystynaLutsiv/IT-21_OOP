class Originator:
    def __init__(self, state: str):
        self._state = state
    def set_state(self, state: str):
        print(f"Зміна стану на: {state}")
        self._state = state
    def get_state(self) -> str:
        return self._state
    def save_to_memento(self):
        return Memento(self._state)
    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print(f"Стан відновлено до: {self._state}")
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_saved_state(self) -> str:
        return self._state

class Caretaker:
    def __init__(self):
        self._mementos = []
    def add_memento(self, memento):
        self._mementos.append(memento)
    def get_memento(self, index):
        return self._mementos[index]

if __name__ == "__main__":
    originator = Originator("Стан #1")
    caretaker = Caretaker()
    caretaker.add_memento(originator.save_to_memento())
    originator.set_state("Стан #2")
    caretaker.add_memento(originator.save_to_memento())
    originator.set_state("Стан #3")
    originator.restore_from_memento(caretaker.get_memento(1))
    originator.restore_from_memento(caretaker.get_memento(0))
