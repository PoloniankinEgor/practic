import re  # Импортируем модуль для проверки шаблонов (используется в определении типа карты)

# --- Проверка корректности введённого номера
def isValidNumber(string):
    # Проверяем, что строка состоит только из цифр
    # и длина соответствует стандартным номерам карт (13, 15 или 16)
    return string.isdigit() and len(string) in [13, 15, 16]


# Функция для вычисления контрольной суммы (алгоритм Луна)
def getCheckSum(string):
    total = 0
    reverse_digits = string[::-1]  # Переворачиваем строку (чтобы удобно считать справа налево)

    # Перебираем цифры с конца
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Каждая вторая цифра (начиная со второй справа) удваивается
        if i % 2 == 1:
            n *= 2
            # Если после удвоения число больше 9 — вычитаем 9 (эквивалент сумме цифр)
            if n > 9:
                n -= 9
        total += n  # Добавляем значение в общую сумму

    return total  # Возвращаем итоговую сумму


#  Определение типа карты по длине и префиксу
def getCardType(string):
    # Visa: 13 или 16 цифр, начинается с "4"
    if (len(string) in [13, 16]) and string.startswith("4"):
        return "Visa"

    # American Express: 15 цифр, начинается с "34" или "37"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"

    # MasterCard: 16 цифр, начинается с диапазона 51–55
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"

    # Если не соответствует ни одному шаблону — неизвестная карта
    return "Invalid"


# Основная программа
number_card = input("Введите номер карты: ")  # Запрашиваем ввод номера

# Проверяем корректность формата
if isValidNumber(number_card):
    # Проверяем контрольную сумму по алгоритму Луна
    if getCheckSum(number_card) % 10 == 0:
        # Если сумма кратна 10 — карта действительна, выводим её тип
        print(getCardType(number_card))
    else:
        # Контрольная сумма не прошла — неверный номер карты
        print("Invalid")
else:
    # Номер содержит недопустимые символы или неверную длину
    print("Invalid")


