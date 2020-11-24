with open("text_fl_2.txt", 'r', encoding='utf-8') as tf:
    str_text = tf.readlines()
    for ind, el in enumerate(str_text, 1):
        w = len(el.split())
        print(f'Строка номер {ind}. Количество слов в строке: {w}')

