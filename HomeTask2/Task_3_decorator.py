# Задача 3: Написать программу, которая принимает на вход список чисел и с помощью декоратора выводит время выполнения функции,
# которая сортирует его по возрастанию.

from typing import List
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.10000f}s")
        return result
    return wrapper



@timer
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers=sorted(numbers)
    return (numbers)


def test_sort_numbers():
    assert sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert sort_numbers([]) == []
    assert sort_numbers([1]) == [1]
    assert sort_numbers([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert sort_numbers([1, 2, 3, 4]) == [1, 2, 3, 4]
    print("All test_sort_numbers pass")
sort_numbers([1, 2, 3, 4])
test_sort_numbers()