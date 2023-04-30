def isNumber(element): # Функция для проверки ввода пользователем числа числа с плавающей точкой
    try:
        float(element)
        return True
    except ValueError:
        return False
