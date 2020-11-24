def my_func(x, y, z):
    ''' функция функция суммы двух максимальных чисел'''
    list = (x, y, z)
    m = min(list)
    s = sum(list)
    result = s - m
    print(f'результат: {result}')

my_func(int(input('введите число "х": ')), int(input('введите число "y": ')), int(input('введите число "z": ')))