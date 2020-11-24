n = int(input('введите число :'))
rating = [9, 7, 6, 3, 3, ]
for el in rating:
    if n > el:
        rating.insert(0, n)
        break
    if n == el:
        ind = rating.index(el)
        c = rating.count(el)
        rating.insert(ind + c, n)
        break
    if n < el:
        rating.append(n)
        rating.sort()
        rating.reverse()
        break
print(f"Итого: {rating}")
