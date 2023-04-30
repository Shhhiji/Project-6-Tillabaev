def getnum(num):
    try:
        a = input("Введите {} сторону треугольника: ".format(num))
        res = float(a)
        return res
    except ValueError:
        print("Вы ввели строчное значение {}.\nПожалуйста, введите положительное числовое значение!".format(a))
        print(" ")
        return None
