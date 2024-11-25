class TileCalculator:
    """
    Клас для розрахунку кількості плитки та витрат на матеріали.
    """
    def __init__(self, tile_width, tile_height, tile_price):
        self.tile_width = tile_width  # ширина плитки в см
        self.tile_height = tile_height  # висота плитки в см
        self.tile_price = tile_price  # ціна за плитку в грн

    def calculate_tiles_needed(self, floor_width, floor_height):
        """
        Обчислює кількість плитки, необхідної для покриття площі підлоги.
        """
        tile_area = self.tile_width * self.tile_height
        floor_area = floor_width * floor_height
        tiles_needed = floor_area / tile_area
        return int(tiles_needed) + 1  # додаємо запас на випадок поділу

    def calculate_total_cost(self, floor_width, floor_height):
        """
        Обчислює загальну вартість плитки, необхідної для покриття підлоги.
        """
        tiles_needed = self.calculate_tiles_needed(floor_width, floor_height)
        return tiles_needed * self.tile_price


class TileLayer:
    """
    Клас для укладання плитки на підлогу.
    """
    def __init__(self, tile_calculator: TileCalculator):
        self.tile_calculator = tile_calculator

    def lay_tiles(self, floor_width, floor_height):
        """
        Функція, що відповідає за процес укладання плитки на підлогу.
        """
        tiles_needed = self.tile_calculator.calculate_tiles_needed(floor_width, floor_height)
        total_cost = self.tile_calculator.calculate_total_cost(floor_width, floor_height)
        print(f"Для укладання плитки потрібно: {tiles_needed} плиток")
        print(f"Загальна вартість плитки: {total_cost} грн")
        print("Укладання плитки на підлогу розпочато...")

# Використання
tile_calculator = TileCalculator(tile_width=30, tile_height=30, tile_price=50)
tile_layer = TileLayer(tile_calculator)

# Припустимо, розміри підлоги 300 см на 200 см
tile_layer.lay_tiles(floor_width=300, floor_height=200)

#Рефакторинг#

class TileCalculator:
    """
    Клас для розрахунку кількості плитки та витрат на матеріали.
    """
    def __init__(self, tile_width, tile_height, tile_price, extra_tiles=1):
        """
        Ініціалізує розміри плитки та її вартість.
        :param tile_width: Ширина плитки (см)
        :param tile_height: Висота плитки (см)
        :param tile_price: Ціна однієї плитки (грн)
        :param extra_tiles: Додатковий запас плитки
        """
        if tile_width <= 0 or tile_height <= 0 or tile_price <= 0:
            raise ValueError("Розміри та ціна плитки мають бути більше 0")
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_price = tile_price
        self.extra_tiles = extra_tiles

    def calculate_tiles_needed(self, floor_width, floor_height):
        """
        Обчислює кількість плитки, необхідної для покриття площі підлоги.
        :param floor_width: Ширина підлоги (см)
        :param floor_height: Довжина підлоги (см)
        :return: Кількість плиток
        """
        if floor_width <= 0 or floor_height <= 0:
            raise ValueError("Розміри підлоги мають бути більше 0")

        tile_area = self.tile_width * self.tile_height
        floor_area = floor_width * floor_height

        if tile_area == 0:
            raise ZeroDivisionError("Площа плитки не може бути 0")

        tiles_needed = floor_area / tile_area
        return int(tiles_needed) + self.extra_tiles  # додаємо запас

    def calculate_total_cost(self, floor_width, floor_height):
        """
        Обчислює загальну вартість плитки, необхідної для покриття підлоги.
        :param floor_width: Ширина підлоги (см)
        :param floor_height: Довжина підлоги (см)
        :return: Загальна вартість (грн)
        """
        tiles_needed = self.calculate_tiles_needed(floor_width, floor_height)
        return tiles_needed * self.tile_price


class TileLayer:
    """
    Клас для управління процесом укладання плитки.
    """
    def __init__(self, tile_calculator: TileCalculator):
        """
        Ініціалізує клас розрахунку плитки.
        :param tile_calculator: Екземпляр TileCalculator
        """
        self.tile_calculator = tile_calculator

    def lay_tiles(self, floor_width, floor_height):
        """
        Виконує розрахунки та імітує процес укладання плитки.
        :param floor_width: Ширина підлоги (см)
        :param floor_height: Довжина підлоги (см)
        """
        tiles_needed = self.tile_calculator.calculate_tiles_needed(floor_width, floor_height)
        total_cost = self.tile_calculator.calculate_total_cost(floor_width, floor_height)
        self._display_results(tiles_needed, total_cost)

    @staticmethod
    def _display_results(tiles_needed, total_cost):
        """
        Виводить результати розрахунків.
        :param tiles_needed: Кількість плиток
        :param total_cost: Загальна вартість
        """
        print(f"Для укладання плитки потрібно: {tiles_needed} плиток")
        print(f"Загальна вартість плитки: {total_cost} грн")
        print("Укладання плитки на підлогу розпочато...")

# Використання
if __name__ == "__main__":
    tile_calculator = TileCalculator(tile_width=30, tile_height=30, tile_price=50, extra_tiles=2)
    tile_layer = TileLayer(tile_calculator)

    # Припустимо, розміри підлоги 300 см на 200 см
    tile_layer.lay_tiles(floor_width=300, floor_height=200)
