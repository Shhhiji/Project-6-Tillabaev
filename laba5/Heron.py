import math

def checkside(a):
    if a > 0:
        return True
    else:
        print("Вы ввели значение {}, которое меньше или равно нулю. Пожалуйста, попытайтесь ввести положительное значение!".format(a))
        return False

def check(a, b, c):
    if a + b >= c:
        if a + c >= b:
            if b + c >= a:
                print("При заданных вами значениями треугольник существует!")
                return True
            else:
                print("\nОшибка в стороне 1) = {}!!!!\n ".format(a))
        else:
            print("\nОшибка в стороне 2) = {}!!!!\n ".format(b))
    else:
        print("\nОшибка в стороне 3) = {}!!!!\n ".format(c))
    return False


def process(a, b, c):  # Функция расчета треугольника по формуле Герона
    p = (a+b+c)/2   # Полупериметр
    S = math.sqrt(p*(p-a)*(p-b)*(p-c)) # формула Герона
    if S == 0:
        print("\nКажется вы ввели неверные значения.\nПлощадь треугольника равна нулю. Попробуйте снова\n")
        return False
    else:
        return True

def access(a, b, c): # Функция отвечающая за проверку значения сторон треугольника, если три истинны значение возвращается
    res1 = checkside(a)
    res2 = checkside(b)
    res3 = checkside(c)
    return res1 and res2 and res3