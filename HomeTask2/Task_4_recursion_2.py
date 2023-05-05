# Задача 4: Напишем рекурсивную функцию, которая вычисляет сумму цифр числа.
# def sum_of_digits(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum
#
# print(sum_of_digits(10))

def sum_of_digits(n: int) -> int:
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

sum_of_digits(12345)

def test_sum_of_digits():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5
    assert sum_of_digits(10) == 1
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(999999999999999) == 135
    print("All test_sum_of_digits pass")

test_sum_of_digits()