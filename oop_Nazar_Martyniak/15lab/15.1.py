class OrderProcessor:
    def __init__(self, order):
        # Ініціалізація об'єкта OrderProcessor з переданим замовленням
        # order - це об'єкт або словник, який містить інформацію про замовлення
        self.order = order

    def process_order(self):
        # Метод, який обробляє замовлення
        # 1. Обчислює загальну суму замовлення
        total = self.calculate_total()
        
        # 2. Обчислює податок на загальну суму
        tax = self.calculate_tax(total)
        
        # 3. Генерує квитанцію із сумою та податком
        self.generate_receipt(total, tax)
        
        # Виводимо інформацію про оброблене замовлення на екран
        print(f"Order processed. Total: {total}, Tax: {tax}")

    def calculate_total(self):
        # Метод для обчислення загальної суми замовлення
        # Використовуємо вбудовану функцію sum для підсумовування всіх цін товарів у списку 'items'
        total = sum(item['price'] for item in self.order['items'])  # Підсумовуємо ціни всіх товарів
        return total  # Повертаємо загальну суму замовлення

    def calculate_tax(self, total):
        # Метод для обчислення податку на загальну суму
        # Податок розраховується як 20% від загальної суми
        return total * 0.2  # 20% податок

    def generate_receipt(self, total, tax):
        # Метод для генерації квитанції
        # Виводимо на екран суму замовлення та податок
        print(f"Receipt: Total: {total}, Tax: {tax}")
        # Тут можна додати додаткові операції для збереження квитанції або її друку
