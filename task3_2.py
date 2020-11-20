
def my_func(name, surname, age, city, email, phone):
    """Анкета"""
    result = f'{name} {surname}, {age}, {city}, {email}, {phone}'
    print(result)

my_func(name = input('Имя: '), surname = input('Фамилия: '), age = input('год рождения: '),
        city = input('город: '), email = input('email: '), phone = input('телефон: '),)