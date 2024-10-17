class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x: int, y: int):
        print(f"Drawing tree of type {self.name} at ({x}, {y}) with color {self.color} and texture {self.texture}")

class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)

if __name__ == "__main__":
    forest = Forest()

    forest.plant_tree(10, 20, "Oak", "Green", "Rough")
    forest.plant_tree(30, 40, "Pine", "Dark Green", "Smooth")
    forest.plant_tree(50, 60, "Oak", "Green", "Rough")
    forest.plant_tree(70, 80, "Birch", "White", "Smooth")

    canvas = "Canvas Object"
    forest.draw(canvas)

    print(f"Unique tree types: {len(TreeFactory._tree_types)}")
