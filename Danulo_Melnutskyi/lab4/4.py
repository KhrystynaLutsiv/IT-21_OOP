def greet(name):
    return f"Привіт, {name}!"

print(greet("Валєра"))

def power(base, exponent=2):
    return base ** exponent

print(power(3))  # повертає 9
print(power(3, 3))  # повертає 27

def apply_func(func, arg):
    return func(arg)

def square(x):
    return x * x

print(apply_func(square, 5))  # повертає 25
