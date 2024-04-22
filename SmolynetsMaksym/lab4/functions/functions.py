# 1. Create a function named my_function.
def my_function():
    print("Hello from a function")


# 2. Execute a function named my_function1.
def my_functiono():
    print("Hello from a function")

my_functiono()

# 3. Inside a function with two parameters, print the first parameter.
def my_functiol(fname, lname):
    print(fname)
# 4. Let the function return the x parameter + 5.
def my_functiong(x):
    return x + 5

# 5. If you do not know the number of arguments that will be passed into your
# function, there is a prefix you can add in the function definition, which prefix?
def my_functionm(*kids):
    print("The youngest child is " + kids[2])

# 6. If you do not know the number of keyword arguments that will be passed into your
# function, there is a prefix you can add in the function definition, which prefix?
def my_functionb(**kid):
    print("His last name is " + kid["lname"])