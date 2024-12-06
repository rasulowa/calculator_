text_to_number = {
    "ноль": 0,"один": 1,"два": 2,"три": 3,"четыре": 4,"пять": 5,"шесть": 6,"семь": 7,"восемь": 8,"девять": 9,"десять": 10,
    "одиннадцать": 11,"двенадцать": 12,"тринадцать": 13,"четырнадцать": 14,"пятнадцать": 15,"шестнадцать": 16,"семнадцать": 17,"восемнадцать": 18,"девятнадцать": 19,"двадцать": 20,
    "тридцать": 30,"сорок": 40,"пятьдесят": 50,"шестьдесят": 60,"семьдесят": 70,"восемьдесят": 80,"девяносто": 90,"сто": 100
}

operations = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "разделить": "//",
    "минус(минус)": "+"
}

def main():
    # Запрашивает у пользователя математические выражения, записанные словами.
    # Программа запрашивает математические выражения, пока пользователь на введёт "выход"

    print(
        """Введите "число <операция> число" в словесной форме. 
Например, двадцать пять плюс тринадцать один."""
    )

    while True:
        string = input("Выражение: ").lower().strip()
        if string == "выход":
            break

        try:
            print(translate_number(eval(translate_words(string))))
        except ValueError as err1:
            print(err1)
        except TypeError:
            print("Неправильная запись операций!")
        except:
            pass


def translate_words(string):
    # Переводит выражение, записанное словами, в математическую форму

    words = string.split()
    expression = []
    num = None

    for word in words:
        if word in text_to_number:
            num = text_to_number[word] if num == None else num + text_to_number[word]
        elif word in operations and check_num(num):
            expression.extend([str(num), operations[word]])
            num = None
        else:
            raise ValueError(f'Незнакомое слово "{word}"!')

    if check_num(num):
        expression.append(str(num))

    return " ".join(expression)


def check_num(num):
    if (0 <= num <= 100) == False:
        raise ValueError("Все числа должны быть от 0 до 100!")
    return True


def translate_number(num):
    # Переводит число в словесную форму

    result = []
    if num < 0:
        result.append("минус")
        num = -num

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
            "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ['', '', "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ['', "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    
    result.append(hundreds[num // 100 % 10])
    if 10 <= (num % 100) <= 19:
        result.append(units[num % 100])
    else:
        result.append(tens[num // 10 % 10])
        result.append(units[num % 10])

    result = list(filter(None, result))
    if len(result) == 0:
        return 'ноль'
    else:
        return " ".join(result)

main()