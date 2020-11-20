def my_f(n):
    lt = n.split(' ')
    s = 0
    for i in lt:
        try:
            i = int(i)
            s = s + i
            # return s
        except:
            ValueError
            print('end')

    print(s)

    my_f(input('введите числа повтроно, для выхода введите любую букву: '))
my_f(input('введите числа через пробел: '))
