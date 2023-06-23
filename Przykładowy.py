def square(x):
    return x * x

def square(x):
    return x * x

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Nie można dzielić przez 0"

print(divide(10, 2))
print(multiply(5, 3))
print(square(5))