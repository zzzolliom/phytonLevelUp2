# Создание класса "Калькулятор" с методами для выполнения математических операций (сложение, вычитание, умножение, деление).
# Реализовать также возможность сохранения результатов операций в памяти калькулятора и их отображения.

# импортируем класс
class Calculator:
    def __init__(self):
        self.memory = []
        self.add_result = None
        self.subtract_result = None
        self.multiply_result = None
        self.divide_result = None


    def add (self, a, b):
        self.add_result = a+b
        return self.add_result



    def subtract (self, a, b):
        self.subtract_result = a-b
        return self.subtract_result

    def multiply(self, a, b):
        self.multiply_result = a * b
        return self.multiply_result



    def divide(self, a, b):
        self.divide_result = a / b
        return self.divide_result


    def memorize_result(self):
        if self.add_result is not None:
            self.memory.append(self.add_result)
        if self.subtract_result is not None:
            self.memory.append(self.subtract_result)
        if self.multiply_result is not None:
            self.memory.append(self.multiply_result)
        if self.divide_result is not None:
            self.memory.append(self.divide_result)


    def show_results(self):
        print(f' р-т сложения={self.add_result}')
        print(f'р-т вычитания={self.subtract_result}')
        print(f'р-т умножения={self.multiply_result}')
        print(f' р-т деления={self.divide_result}')

    def show_memory(self):
        print(self.memory)

# создаем объект калькулятора
calc = Calculator()

# выполняем операции
calc.add(5, 3)
calc.subtract(5, 3)
calc.multiply(5, 3)
calc.divide(5, 3)

# сохраняем результат в память калькулятора
calc.memorize_result()

# отображаем результаты операций
calc.show_results()

# отображаем результат, сохраненный в памяти калькулятора
calc.show_memory()