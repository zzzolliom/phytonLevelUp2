# a = '10*5-7*3+2'



# def made_lst(a):
#     lst = []
#     lst2 = []
#     for i in a:
#         lst.append(i)
#     for i in range(len(lst)):
#         if i >0:
#             if lst[i].isdigit():
#                 if lst[i - 1].isdigit():
#                     lst2.append (int(lst[i - 1] + lst[i]))
#                 else:
#                     lst2.append (int(lst[i]))
#             else:
#                 if i==1:
#                     lst2.append (int(lst[i-1]))
#                     lst2.append(lst[i])
#                 else:
#                     lst2.append(lst[i])

#     print(lst2)
#     # print(lst)
#     return lst2


# # lst_3=made_lst(a)

# def calculate(lst):
#     lst_calculate = []
#     i = 0
#     while i < len(lst):
#         if isinstance(lst[i], int):
#             lst_calculate.append(lst[i])
#             i += 1
#         elif lst[i] == '+':
#             a = lst_calculate.pop()
#             lst_calculate.append(lst[i + 1])
#             b = lst_calculate.pop()
#             lst_calculate.append(a + b)
#             i += 2
#             print('lst_calculate в цикле с +', lst_calculate)
#         elif lst[i] == '-':
#             c = lst_calculate.pop()
#             print('c в цикле с -', c)
#             lst_calculate.append(lst[i + 1])
#             print('lst  в цикле с - середина  ', lst_calculate)
#             b = lst_calculate.pop()
#             print('b в цикле с -', b)

#             lst_calculate.append(c - b)
#             i += 2
#             print('lst в цикле с -', lst_calculate)
#         elif lst[i] == '*':
#             a = lst_calculate.pop()
#             lst_calculate.append(lst[i + 1])
#             b = lst_calculate.pop()
#             lst_calculate.append(a * b)
#             i += 2
#             print('lst в цикле с+', lst_calculate)

#         elif lst[i] == '/':
#             a = lst_calculate.pop()
#             lst_calculate.append(lst[i + 1])
#             b = lst_calculate.pop()
#             lst_calculate.append(a * b)
#             i += 2
#             print('lst в цикле с +', lst_calculate)

#     result = lst_calculate.pop()
#     return result
#     # print(result)


# # calculate_(lst_3)

# Исправленное решение:
def calculate(expr):
    lst = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            lst.append(num)
            continue
        elif expr[i] == ' ':
            i += 1
            continue
        elif expr[i] in ['+', '-', '*', '/']:
            lst.append(expr[i])
            i += 1
            continue
        else:
            raise ValueError('Invalid character in expression')
    i = 1
    while i < len(lst):
        if lst[i] == '*':
            lst[i-1:i+2] = [lst[i-1] * lst[i+1]]
        elif lst[i] == '/':
            lst[i-1:i+2] = [lst[i-1] / lst[i+1]]
        else:
            i += 1
    result = lst[0]
    for i in range(1, len(lst), 2):
        if lst[i] == '+':
            result += lst[i+1]
        else:
            result -= lst[i+1]
    return result


assert calculate("2+3*4-5/2") == 11.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 31
