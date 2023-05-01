# Задача: Написать программу, которая принимает на вход список целых чисел и удаляет из него все нечетные числа.
# При этом использовать только базовые операции, цикл for, функции и контейнерные типы данных.


# all_numbers=[1,7,8,9,11]
# for i in all_numbers:
#     if (i%2) ==1:
#         all_numbers.remove(i)
# print('all_numbers',all_numbers)   ---- с циклом for не работает

all_numbers_2=[1,2,3,4,5,44,444,4445]
i=0
while i<len(all_numbers_2):
    if (all_numbers_2[i]%2) ==1:
        all_numbers_2.pop(i)
    i+=1
print('all_numbers_2',all_numbers_2)


# all_numbers11=[1,77,8,9,88,104,999] - тут не выполняется условие задачи=(
# even_numbers =[]
# for i in all_numbers11:
#     if i%2 ==0:
#         even_numbers.append(i)
#
# print(even_numbers)

