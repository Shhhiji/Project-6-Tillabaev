def getrnum(num): # Функция на проверку ошибок введеным пользователем
    try:
        a = input("Введите {} сторону треугольника : ".format(num))
        res = float(a)
        return res
    except ValueError: # обработка ошибки
        print("Вы ввели строчное значение {}. Введите положительное числовое значение!".format(a))
        return None