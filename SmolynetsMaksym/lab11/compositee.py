class MenuComponent:
    def add(self, component):
        raise NotImplementedError

    def remove(self, component):
        raise NotImplementedError

    def show(self):
        raise NotImplementedError


class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"Страва: {self.name}, Ціна: {self.price} грн")


class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component):
        self.items.append(component)

    def remove(self, component):
        self.items.remove(component)

    def show(self):
        print(f"\nМеню: {self.name}")
        for item in self.items:
            item.show()


main_menu = Menu("Головне меню")

lunch_menu = Menu("Обіди")
lunch_menu.add(MenuItem("Борщ", 50))
lunch_menu.add(MenuItem("Картопляне пюре", 30))

drinks_menu = Menu("Напої")
drinks_menu.add(MenuItem("Кава", 20))
drinks_menu.add(MenuItem("Чай", 15))

main_menu.add(lunch_menu)
main_menu.add(drinks_menu)

main_menu.show()
