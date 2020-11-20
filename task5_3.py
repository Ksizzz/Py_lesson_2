with open("text_3.txt", 'r', encoding='utf-8') as tf:
    str_text = {line.split()[0]: float(line.split()[1]) for line in tf}
    s = 0
    c = 0
    for key, value in str_text.items():
        if float(value) <= 20000:
            s = s + float(value)
            c += 1
            print(f'Фамилия: {key}, ЗП: {value}')
    med = s / c
    print(f'Cредняя величина ЗП этих сотрудников: {round(med, 3)}')
