a = '10*5-7*3+2'



def made_lst(a):
    lst = []
    lst2 = []
    for i in a:
        lst.append(i)
    for i in range(len(lst)):
        if i >0:
            if lst[i].isdigit():
                if lst[i - 1].isdigit():
                    lst2.append (int(lst[i - 1] + lst[i]))
                else:
                    lst2.append (int(lst[i]))
            else:
                if i==1:
                    lst2.append (int(lst[i-1]))
                    lst2.append(lst[i])
                else:
                    lst2.append(lst[i])

    print(lst2)
    # print(lst)
    return lst2


lst_3=made_lst(a)

def calculate_(lst):
    lst_calculate = []
    i = 0
    while i < len(lst):
        if isinstance(lst[i], int):
            lst_calculate.append(lst[i])
            i += 1
        elif lst[i] == '+':
            a = lst_calculate.pop()
            lst_calculate.append(lst[i + 1])
            b = lst_calculate.pop()
            lst_calculate.append(a + b)
            i += 2
            print('lst_calculate в цикле с +', lst_calculate)
        elif lst[i] == '-':
            c = lst_calculate.pop()
            print('c в цикле с -', c)
            lst_calculate.append(lst[i + 1])
            print('lst  в цикле с - середина  ', lst_calculate)
            b = lst_calculate.pop()
            print('b в цикле с -', b)

            lst_calculate.append(c - b)
            i += 2
            print('lst в цикле с -', lst_calculate)
        elif lst[i] == '*':
            a = lst_calculate.pop()
            lst_calculate.append(lst[i + 1])
            b = lst_calculate.pop()
            lst_calculate.append(a * b)
            i += 2
            print('lst в цикле с+', lst_calculate)

        elif lst[i] == '/':
            a = lst_calculate.pop()
            lst_calculate.append(lst[i + 1])
            b = lst_calculate.pop()
            lst_calculate.append(a * b)
            i += 2
            print('lst в цикле с +', lst_calculate)

    result = lst_calculate.pop()
    print(result)


calculate_(lst_3)
