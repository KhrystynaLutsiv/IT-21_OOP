# Клас, який представляє замовлення
class Order:
    def __init__(self, items):
        # Ініціалізуємо замовлення списком товарів
        self.items = items

    def calculate_total(self):
        # Обчислюємо загальну суму замовлення шляхом підсумовування цін усіх товарів
        return sum(item['price'] for item in self.items)


# Клас, який відповідає за розрахунок податків
class TaxCalculator:
    def calculate_tax(self, total):
        # Розраховуємо податок (20% від загальної суми)
        return total * 0.2  # 20% податок


# Клас, який відповідає за генерацію квитанцій
class ReceiptGenerator:
    def generate(self, total, tax):
        # Генеруємо та виводимо квитанцію на екран
        print(f"Receipt: Total: {total}, Tax: {tax}")


# Клас, який обробляє замовлення, використовуючи інші сервіси (замовлення, податки та квитанції)
class OrderProcessor:
    def __init__(self, order, tax_calculator, receipt_generator):
        # Ініціалізуємо OrderProcessor з об'єктами замовлення, калькулятора податків і генератора квитанцій
        self.order = order
        self.tax_calculator = tax_calculator
        self.receipt_generator = receipt_generator

    def process_order(self):
        # Обробка замовлення
        total = self.order.calculate_total()  # Обчислюємо загальну суму замовлення
        tax = self.tax_calculator.calculate_tax(total)  # Обчислюємо податок
        self.receipt_generator.generate(total, tax)  # Генеруємо квитанцію
        # Виводимо загальну суму та податок
        print(f"Order processed. Total: {total}, Tax: {tax}")




# Створюємо об'єкти для обробки замовлення
order = Order(items=[{'price': 100}, {'price': 200}])  # Замовлення з товарами
tax_calculator = TaxCalculator()  # Об'єкт для розрахунку податків
receipt_generator = ReceiptGenerator()  # Об'єкт для генерації квитанцій

# Створюємо об'єкт для обробки замовлення
order_processor = OrderProcessor(order, tax_calculator, receipt_generator)

# Обробляємо замовлення
order_processor.process_order()
