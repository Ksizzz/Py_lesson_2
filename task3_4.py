def my_func(x, y):
    ''' функция функция возведения в степень отрицательного числа'''
    result = 1
    for i in range(abs(y)):
        result = result * x
    result = 1 / result
    print(f'Результат: {result.__round__(2)}')

my_func(int(input('введите целое положительное число "x": ')), int(input('введите отрицательное число "y": ')))
