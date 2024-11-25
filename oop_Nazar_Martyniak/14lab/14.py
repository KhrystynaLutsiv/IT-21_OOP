from abc import ABC, abstractmethod

# Базовий інтерфейс для стратегії знижки
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

# Стратегія знижки у вигляді відсотка
class PercentDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9  # 10% знижка

# Стратегія фіксованої знижки
class FixedDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price - 20  # фіксована знижка 20

# Стратегія знижки для постійних клієнтів
class LoyaltyDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.85  # знижка 15% для постійних клієнтів

# Клас для обчислення знижки, який використовує стратегію
class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy  # приймає стратегію як параметр
    
    def calculate(self, price):
        return self.strategy.apply_discount(price)  # обчислює знижку, застосовуючи стратегію

# Тестування коду:
price = 100  # Початкова ціна

# Використовуємо стратегію знижки для постійних клієнтів
calculator = DiscountCalculator(LoyaltyDiscount())
print(f"Ціна після знижки для постійного клієнта: {calculator.calculate(price)}")  # 85.0

# Використовуємо фіксовану знижку
calculator = DiscountCalculator(FixedDiscount())
print(f"Ціна після фіксованої знижки: {calculator.calculate(price)}")  # 80.0

# Використовуємо знижку у вигляді відсотка
calculator = DiscountCalculator(PercentDiscount())
print(f"Ціна після знижки у вигляді відсотка: {calculator.calculate(price)}")  # 90.0
