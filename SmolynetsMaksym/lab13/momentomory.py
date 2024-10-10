class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state
        print(f"State set to: {self.state}")

    def save_state_to_memento(self):
        return Memento(self.state)

    def restore_state_from_memento(self, memento):
        self.state = memento.state
        print(f"State restored to: {self.state}")


class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


# Використання шаблону Memento
originator = Originator()
caretaker = Caretaker()

originator.set_state("State 1")
caretaker.add_memento(originator.save_state_to_memento())

originator.set_state("State 2")
caretaker.add_memento(originator.save_state_to_memento())

originator.set_state("State 3")
print("Restoring to previous state...")
originator.restore_state_from_memento(caretaker.get_memento(0))
