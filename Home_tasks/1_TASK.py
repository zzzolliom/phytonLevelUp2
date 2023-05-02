# a = int(input("Введите любое число:"))
# b = int(input("Введите любое число:"))
# print( f'{a} * {b} =', a*b)
# c = a*b

def multiply(a, b):
    return a*b

assert multiply(2, 3) == 6
assert multiply(10, 5) == 50
assert multiply(7, -3) == -21
