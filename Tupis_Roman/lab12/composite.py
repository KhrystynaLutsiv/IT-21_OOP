class Component:
    def operation(self):
        raise NotImplementedError("You should implement this method.")


class Leaf(Component):
    def operation(self):
        print("Leaf operation")


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        print("Composite operation")
        for child in self.children:
            child.operation()


# Приклад використання
if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()
    composite = Composite()

    composite.add(leaf1)
    composite.add(leaf2)

    composite.operation()  # Виведе операції листків
