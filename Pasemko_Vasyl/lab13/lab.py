class State:
    def handle(self):
        pass

class OnState(State):
    def handle(self):
        print("Device is ON")

class OffState(State):
    def handle(self):
        print("Device is OFF")

class Device:
    def __init__(self):
        self.state = OffState()

    def toggle(self):
        if isinstance(self.state, OffState):
            self.state = OnState()
        else:
            self.state = OffState()

    def perform_action(self):
        self.state.handle()

# Використання
device = Device()
device.perform_action()  # Виведе "Device is OFF"
device.toggle()
device.perform_action()  # Виведе "Device is ON"
device.toggle()
device.perform_action()  # Знову виведе "Device is OFF"
