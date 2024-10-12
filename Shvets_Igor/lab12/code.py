class Aircraft:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display(self, x, y):
        print(f"Displaying {self.color} {self.model} at position ({x}, {y})")


class AircraftFactory:

    def __init__(self):
        self.aircrafts = {}

    def get_aircraft(self, model, color):
        key = (model, color)
        if key not in self.aircrafts:
            self.aircrafts[key] = Aircraft(model, color)
            print(f"Creating new Aircraft: {model}, {color}")
        return self.aircrafts[key]

class Game:

    def __init__(self):
        self.factory = AircraftFactory()

    def add_aircraft(self, model, color, x, y):
        aircraft = self.factory.get_aircraft(model, color)
        aircraft.display(x, y)

if __name__ == "__main__":
    game = Game()
    game.add_aircraft("F-16", "Red", 100, 200)
    game.add_aircraft("F-16", "Red", 150, 250)
    game.add_aircraft("F-22", "Blue", 300, 400)
    game.add_aircraft("F-22", "Blue", 350, 450)
