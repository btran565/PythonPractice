def factorial(num):
    value = 1
    for i in range(num, 0, -1):
        value *= i
    return value
