# Задача: Написать программу, которая принимает на вход три числа и определяет, являются ли они пифагоровой тройкой.
# При этом использовать только базовые операции и условные операторы.

lst=[3,6,4]
lst.sort()


def answer(lst): # Почему список? Мы всегда хотим проверять только 3 числа, это значение не меняется
    for i in range(len(lst)): # Если мы не используем переменную можно указать _
        if lst[0]*lst[0]+lst[1]*lst[1]==lst[2]*lst[2]: # Очень сложно прочесть, но решение хорошее
            print('Являетсвя пифагоровой тройкой')
            return True
        else: # Else не нужен мы в if уже вышли из функции
            print('Не являетсвя пифагоровой тройкой')

            # В итоге мы хотим получить true или false а не None

# Ваше решение убрав лишнее
def is_pythagorean_triple(a, b, c):
    if a * a + b * b == c * c:
        return True
    return False

    # Или так
    return True if a * a + b * b == c * c else False



assert is_pythagorean_triple(3, 4, 5) == True
assert is_pythagorean_triple(5, 12, 13) == True
assert is_pythagorean_triple(7, 8, 9) == False
