# Задача 1: Написать программу, которая принимает на вход список чисел и возвращает список, содержащий только нечетные числа, умноженные на два.
# При этом, использовать функции filter, map и лямбда-функцию.
# multiplication_of_odd_numbers = list(map(lambda x: x*2,(filter(lambda x: x % 2 != 0, lst))))
# print(multiplication_of_odd_numbers)


# odd_numbers=list(filter(lambda x:x%2!=0,lst))
# multiplication_of_odd_numbers= list(map(lambda x: x*2,odd_numbers))
# print(multiplication_of_odd_numbers)


def get_odd_doubled_numbers(lst):
    multiplication_of_odd_numbers = list(map(lambda x: x*2,(filter(lambda x: x % 2 != 0, lst))))
    return multiplication_of_odd_numbers


def test_get_odd_doubled_numbers():
    assert get_odd_doubled_numbers([1, 2, 3, 4, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([10, 20, 30]) == []
    assert get_odd_doubled_numbers([]) == []
    assert get_odd_doubled_numbers([1, 3, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([2, 4, 6]) == []
    print("All test_get_odd_doubled_numbers passed!")

test_get_odd_doubled_numbers()