text_fl = open("text_fl.txt", 'w', encoding='utf-8')
while True:
    str_text = input('введите нужный текст: ')
    text_fl.write(f'{str_text}\n')
    if not str_text:
        break
text_fl.close()