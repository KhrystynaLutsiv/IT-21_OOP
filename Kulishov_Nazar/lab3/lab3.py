# Перевірка парності числа
num = 7
if num % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

# Вивід простих чисел в діапазоні
for i in range(2, 20):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, " - просте число")

# Використання циклу while для виведення чисел
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b
