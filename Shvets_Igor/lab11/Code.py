
class Laptop:
    def __init__(self):
        self.brand = None
        self.ram = None
        self.storage = None
        self.processor = None
        self.graphics_card = None

    def __str__(self):
        return (f"Laptop Specifications:\n"
                f"Brand: {self.brand}\n"
                f"RAM: {self.ram} GB\n"
                f"Storage: {self.storage} GB\n"
                f"Processor: {self.processor}\n"
                f"Graphics Card: {self.graphics_card}\n")



class LaptopBuilder:
    def __init__(self):
        self.laptop = Laptop()

    def set_brand(self, brand):
        self.laptop.brand = brand
        return self

    def set_ram(self, ram):
        self.laptop.ram = ram
        return self

    def set_storage(self, storage):
        self.laptop.storage = storage
        return self

    def set_processor(self, processor):
        self.laptop.processor = processor
        return self

    def set_graphics_card(self, graphics_card):
        self.laptop.graphics_card = graphics_card
        return self

    def build(self):
        return self.laptop


if __name__ == "__main__":
    builder = LaptopBuilder()
    laptop = (builder
              .set_brand("Dell")
              .set_ram(16)
              .set_storage(512)
              .set_processor("Intel i7")
              .set_graphics_card("NVIDIA GTX 1650")
              .build())

    print(laptop)
