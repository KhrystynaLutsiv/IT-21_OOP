def sum_numbers(a, b):
    return a + b

def print_result(result):
    print(f"Результат: {result}")

sum = sum_numbers(5, 10)

callback = print_result

callback(sum)
