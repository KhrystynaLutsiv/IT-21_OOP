from abc import ABC, abstractmethod
# Інтерфейс стратегії
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, base_price):
        pass
#для стандартної ціни
class RegularPricingStrategy(PricingStrategy):
    def calculate_price(self, base_price):
        return base_price
#для знижки
class DiscountPricingStrategy(PricingStrategy):
    def __init__(self, discount):
        self.discount = discount

    def calculate_price(self, base_price):
        return base_price * (1 - self.discount)
class Audi:
    def __init__(self, model, engine, color, horsepower, base_price, pricing_strategy: PricingStrategy):
        self.model = model
        self.engine = engine
        self.color = color
        self.horsepower = horsepower
        self.base_price = base_price
        self.pricing_strategy = pricing_strategy
    def set_pricing_strategy(self, pricing_strategy: PricingStrategy):
        self.pricing_strategy = pricing_strategy
    def display_details(self):
        price = self.pricing_strategy.calculate_price(self.base_price)
        return (f'Audi {self.model} (engine: {self.engine}, color: {self.color}, '
                f'horsepower: {self.horsepower} hp, price: ${price:.2f})')

# Strategy
if __name__ == "__main__":
    base_price = 80000
    #регулярна ціна
    audi_regular = Audi("A6", "3.0 TFSI V6", "чорний", 340, base_price, RegularPricingStrategy())
    print(audi_regular.display_details())
    #знижка 15%
    audi_discount = Audi("Q7", "4.0 TFSI V8", "білий", 500, base_price, DiscountPricingStrategy(discount=0.15))
    print(audi_discount.display_details())
