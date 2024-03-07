def sum_numbers(a, b):
    return a + b

# Зчитуємо два числа від користувача
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Викликаємо функцію та виводимо результат
result = sum_numbers(num1, num2)
print("Сума чисел:", result)
