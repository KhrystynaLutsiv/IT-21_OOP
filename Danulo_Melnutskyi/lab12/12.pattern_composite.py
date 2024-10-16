class EuropeanSocket:
    def voltage(self):
        return 230

    def plug_type(self):
        return "Type C"



class AmericanDevice:
    def power_on(self, voltage):
        if voltage == 120:
            print("Пристрій увімкнено!")
        else:
            print("Неправильний вольтаж, пристрій не може увімкнутися.")



class SocketAdapter:
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def voltage(self):
        return 120

    def plug_type(self):
        return "Type A"



european_socket = EuropeanSocket()
american_device = AmericanDevice()


print("Без адаптера:")
american_device.power_on(european_socket.voltage())


print("\nЗ адаптером:")
adapter = SocketAdapter(european_socket)
american_device.power_on(adapter.voltage())

