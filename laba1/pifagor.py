from math import sqrt # Импорт из модуля math функции sqrt для возвращения квадратного корня числа
def checkcat(a): # Проверка первого катета больше нуля или нет
    if a > 0:
        return True
    else:
        print("Ваше значение катета {} меньше или равно нулю. Введите положительное значение!".format(a))
        return False


def getrnum(num): # Функция на проверку ошибок введеным пользователем
    try:
        a = input("Введите катет {} для расчета: ".format(num))
        res = float(a)
        return res
    except ValueError: # обработка ошибки
        print("Вы ввели строчное значение {}. \nВведите положительное числовое значение!".format(a))
        print(" ")
        return None

    
def access(a, b): # Функция отвечающая за проверку значения катетов, если оба истинны значение возвращается
    rec = checkcat(a)
    rec2 = checkcat(b)
    return rec and rec2


def process(a, b): # Функция расчета гипотенузы 
    gip = sqrt(a**2 + b**2)
    return gip

