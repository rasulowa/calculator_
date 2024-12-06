def function(calc):
    # Функция, принимающая строку от пользователя и возвращающая строку

    result = None

    units = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
            'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
            'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
            'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']   # Список, содержащий текстовые представления чисел от 0 до 19.

    tens = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
            'семьдесят', 'восемьдесят', 'девяносто']    # Список, содержащий текстовые представления десятков от 20 до 90

    hundreds = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']   # Список, содержащий текстовые представления сотен от 100 до 900.

    thousands = ['тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи',
                'пять тысяч', 'шесть тысяч', 'семь тысяч', 'восемь тысяч',
                'девять тысяч']   # Список, содержащий текстовые представления тысяч от 1000 до 9000.

    numbers = []

    for ten in tens:   # Создание чисел от 21 до 99
        for num in [''] + units[1:10]:
            if num != '':
                units.append(ten + ' ' + num)
            else:
                units.append(ten + num)

    for hundred in hundreds:   # Создание чисел от 100 до 999
        for ten in [''] + units[1:100]:
            if ten != '':
                units.append(hundred + ' ' + ten)
            else:
                units.append(hundred + ten)

    for thousand in thousands:   # Создание чисел от 1000 и выше
        for hundred in [''] + units[1:1000]:
            if hundred != '':
                units.append(thousand + ' ' + hundred)
            else:
                units.append(thousand + hundred)

    for num in range(0, 10000):  #  Генерация чисел от 0 до 9999
        numbers.append(num)

    if '  ' in calc or calc[0] == ' ' or calc[-1] == ' ':  # Проверка ошибок ввода
        print('Ошибка ввода')
        return True 
        # Замена текстовых команд на математические операции
    calc = calc.replace('минус', '-')
    calc = calc.replace('плюс', '+')
    calc = calc.replace('умножить на', '*')
    calc = calc.replace('скобка открывается', '(')
    calc = calc.replace('скобка закрывается', ')')
    for index, num in enumerate(reversed(units[0:100])):   # Замена единиц на числа
        calc = calc.replace(num, str(numbers[100 - index - 1]))    
    try:   # Обработка вычислений
        result = eval(calc)
    except SyntaxError:
        print('Ошибка ввода')
    except NameError:
        print('Ошибка ввода')
    
    if result != None:    # Дополнительные проверки ввода
        calc = calc.replace(' ', '')
        if ('**' in calc or '++' in calc or calc[0] == '+' or '++' in calc or
            '---' in calc or '-+' in calc or '+--' in calc or '*--' in calc or
            calc.find('--') == 0):
            print('Ошибка ввода')
            return True
        else:
            try:
                print(units[numbers.index(result)])
            except ValueError:
                print('Ошибка ввода')

print("""Введите "число <операция> число" в словесной форме. 
Например, двадцать пять плюс тринадцать один.""")

function(input('Введите выражение: '))
