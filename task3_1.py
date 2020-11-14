def split(num_1, num_2):
    ''' функция деления, где первое число - делимое, а второе - делитель'''
    num_1 = int(input('укажите делимое: '))
    num_2 = int(input('укажите делителль: '))
    try:
        num_2 != 0
        result = num_1 / num_2
        result = round(result, 2)
        print(f'результат: {result}')
    except:
        print('Ошибка. На ноль делить нельзя')

split(1, 1)

