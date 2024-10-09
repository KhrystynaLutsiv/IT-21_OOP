class Audi:
    def __init__(self, model, engine, color, horsepower):
        self.model = model 
        self.engine = engine 
        self.color = color 
        self.horsepower = horsepower  

    def display_details(self):
        return f'Audi {self.model} (engine: {self.engine}, color: {self.color}, horsepower: {self.horsepower} hp)'


class AudiProxy:
    def __init__(self, model, engine, color, horsepower):
        self._audi = None
        self.model = model
        self.engine = engine
        self.color = color
        self.horsepower = horsepower

    def _create_audi(self):
        if self._audi is None:
            print(f"Створюю Audi {self.model}...")
            self._audi = Audi(self.model, self.engine, self.color, self.horsepower)

    def display_details(self):
        self._create_audi()
        return self._audi.display_details()

#патерн Proxy
if __name__ == "__main__":
    audi_proxy = AudiProxy("RS6", "4.0 TFSI V8", "чорний", 600)

    # Автомобіль не створений, але ми можемо запитувати деталі через проксі
    print(audi_proxy.display_details())

    # Викликаємо деталі об'єкт вже створений
    print(audi_proxy.display_details())
