# Задача: Написать программу, которая принимает на вход список строк и возвращает новый список, содержащий только те строки,
# которые начинаются с большой буквы.
# При этом использовать только базовые операции, цикл for, функции и контейнерные типы данных.


# lst=["Apple", "Banana", "cherry"]
# lst_upper=[]
# for i in lst:
#     if i[0].isupper():
#         lst_upper.append(i)
# print(lst_upper)

def filter_capitalized_words(words):
    lst_upper = []
    for i in words:
        if i[0].isupper():
            lst_upper.append(i)
    return lst_upper


assert filter_capitalized_words(["Apple", "Banana", "cherry"]) == ["Apple", "Banana"]
assert filter_capitalized_words(["Python", "java", "C++"]) == ["Python", "C++"]
assert filter_capitalized_words(["Red", "green", "Blue"]) == ["Red", "Blue"]
