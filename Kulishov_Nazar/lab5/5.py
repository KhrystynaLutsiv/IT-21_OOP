class Tree:
    def __init__(self, species, age):
        self.species = species
        self.age = age
        self.height = 0

    def grow(self, height_increase):
        self.height += height_increase
        print(f"The {self.species} tree grew by {height_increase} meters.")

    def info(self):
        print(f"This is a {self.age}-year-old {self.species} tree, {self.height} meters tall.")


# Створення екземпляру класу Tree
oak_tree = Tree("Oak", 10)

# Виклик методів об'єкта
oak_tree.grow(2)
oak_tree.info()
