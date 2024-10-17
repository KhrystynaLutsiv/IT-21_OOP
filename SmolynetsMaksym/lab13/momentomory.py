import abc
from collections import deque
from typing import Deque


class IMemento(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_dollars(self) -> int:
        pass

    def get_euro(self) -> int:
        pass


class ExchangeMemento(IMemento):
    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self) -> int:
        return self.__dollars

    def get_euro(self) -> int:
        return self.__euro


class Exchange:
    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self):
        print('Dollars: {}'.format(self.__dollars))

    def get_euro(self):
        print('Euro: {}'.format(self.__euro))

    def sell(self):
        if self.__dollars > 0:
            self.__dollars -= 1
    def buy(self):
        self.__euro += 1

    def save(self) -> ExchangeMemento:
        return ExchangeMemento(self.__dollars, self.__euro)

    def restore(self, exchange_memento: IMemento):
        self.__dollars = exchange_memento.get_dollars()
        self.__euro = exchange_memento.get_euro()


class Memory:

    def __init__(self, exchange: Exchange):
        self.__exchange = exchange
        self.__history: Deque[IMemento] = []

    def backup(self):
        self.__history.append(self.__exchange.save())

    def undo(self):
        if len(self.__history) == 0:
            return
        else:
            self.__exchange.restore(self.__history.pop())


if __name__ == '__main__':
    exchange = Exchange(5, 5)

    memory = Memory(exchange)

    exchange.get_dollars()
    exchange.get_euro()

    print('------- SELlING DOLLARS ---------')
    exchange.sell()
    exchange.buy()

    exchange.get_dollars()
    exchange.get_euro()

    print('------- SAVING STANE ---------')
    memory.backup()

    print('------- SELL DOLLARS, BUYING EURO --------')
    exchange.sell()
    exchange.buy()

    exchange.get_dollars()
    exchange.get_euro()

    print('------- SYSTEM RESTORE --------')
    memory.undo()

    exchange.get_dollars()
    exchange.get_euro()



'''
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
'''
