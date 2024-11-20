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

