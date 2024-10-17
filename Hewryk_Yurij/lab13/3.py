from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        pass

    def set_next(self, handler):
        self._next_handler = handler

    def pass_to_next(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class LowLevelHandler(Handler):
    def handle(self, request):
        if request < 10:
            print(f"LowLevelHandler: Обробляю запит {request}")
        else:
            print(f"LowLevelHandler: Не можу обробити {request}, передаю далі.")
            return self.pass_to_next(request)

class MidLevelHandler(Handler):
    def handle(self, request):
        if 10 <= request < 50:
            print(f"MidLevelHandler: Обробляю запит {request}")
        else:
            print(f"MidLevelHandler: Не можу обробити {request}, передаю далі.")
            return self.pass_to_next(request)

class HighLevelHandler(Handler):
    def handle(self, request):
        if request >= 50:
            print(f"HighLevelHandler: Обробляю запит {request}")
        else:
            print(f"HighLevelHandler: Не можу обробити {request}, передаю далі.")
            return self.pass_to_next(request)

low_handler = LowLevelHandler()
mid_handler = MidLevelHandler()
high_handler = HighLevelHandler()

low_handler.set_next(mid_handler)
mid_handler.set_next(high_handler)

requests = [5, 20, 75, 45]

for request in requests:
    print(f"\nЗапит {request}:")
    low_handler.handle(request)
