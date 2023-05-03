# Задача: Написать программу, которая принимает на вход строку и возвращает список всех уникальных слов в этой строке.
# При этом использовать только базовые операции, цикл for, функции и контейнерные типы данных.

input_str = input("Введите любую строку:")
punctuation = ".,:;-?!()[]{}<>/\|"
without_punctuation=""
for i in input_str:
    if i not in punctuation:
        without_punctuation+=i
print(without_punctuation)
lst_without_punctuation = without_punctuation.split()

uniq_worlds=set(lst_without_punctuation)
print(uniq_worlds)
