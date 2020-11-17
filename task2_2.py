l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
long = len(l)
v = len(l) % 2
i1 = 0
i2 = 1
f = []
if v == 0:
    print('число значений чётное')
    long -= 1
    while i2 <= long:
        z = l[i1]
        y = l[i2]
        z, y = y, z
        f.append(z)
        f.append(y)
        i1 += 2
        i2 += 2
    print(f)
if v == 1:
    print('число значений нечётное')
    long -= 1
    while i2 <= long:
        z = l[i1]
        y = l[i2]
        z, y = y, z
        f.append(z)
        f.append(y)
        i1 += 2
        i2 += 2
        f.append(l[-1])
    print(f)
