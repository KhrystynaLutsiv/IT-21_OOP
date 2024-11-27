class Game:
    def __init__(self):
        self.p = 100  # очки гравця
        self.e = 3  # кількість ворогів
        self.l = 1  # рівень гри

    def run(self):
        print("Гра почалась!")
        self.p -= 10  # гравець отримує шкоду
        self.e -= 1  # гравець знищив ворога
        if self.e == 0:
            self.l += 1
            print("Рівень підвищено!")
        print(f"Очки гравця: {self.p}, Вороги: {self.e}, Рівень: {self.l}")


game = Game()
game.run()

#Рефакторинг#

class Game:
    """
    Клас для управління логікою гри.
    """
    def __init__(self):
        self.player_health = 100  # Здоров'я гравця
        self.enemies_remaining = 3  # Кількість ворогів
        self.level = 1  # Рівень гри

    def start_game(self):
        """
        Починає гру.
        """
        print("Гра почалась!")
        self.player_takes_damage(10)
        self.enemy_defeated()
        if self.enemies_remaining == 0:
            self.level_up()
        self.display_status()

    def player_takes_damage(self, damage):
        """
        Зменшує здоров'я гравця.
        :param damage: Шкода, отримана гравцем
        """
        self.player_health -= damage

    def enemy_defeated(self):
        """
        Зменшує кількість ворогів на 1.
        """
        self.enemies_remaining -= 1

    def level_up(self):
        """
        Підвищує рівень гри.
        """
        self.level += 1
        print("Рівень підвищено!")

    def display_status(self):
        """
        Виводить поточний стан гри.
        """
        print(f"Здоров'я гравця: {self.player_health}")
        print(f"Вороги, що залишились: {self.enemies_remaining}")
        print(f"Поточний рівень: {self.level}")


# Запуск гри
if __name__ == "__main__":
    game = Game()
    game.start_game()
