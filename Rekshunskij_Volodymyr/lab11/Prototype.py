import copy

class Audi:
    def __init__(self, model, engine, color, horsepower):
        self.model = model 
        self.engine = engine 
        self.color = color 
        self.horsepower = horsepower  

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f'Audi {self.model} (engine: {self.engine}, color: {self.color}, horsepower: {self.horsepower} hp)'


# Приклад використання патерна Прототип
if __name__ == "__main__":
    original_audi = Audi("RS6", "4.0 TFSI V8", "чорний", 600)
    print(f"Оригінал Audi RS: {original_audi}")

    cloned_audi = original_audi.clone()

    # Зміна властивостей клону
    cloned_audi.color = "білий"
    cloned_audi.model = "RS7"
    cloned_audi.engine = "4.0 TFSI V8"
    cloned_audi.horsepower = 605

    # Виведення результату
    print(f"Клон Audi: {cloned_audi}")

