from statistics import median # вызов функции для посчета медианы
from error import isNumber # Вызов встроенно функции для проверки ввода, ввел пользователь число или нет

def mediana_num():
    try: 
        while True:
            while True:
                medn_enter = input("Подсчет медианы чисел.\nВведите числовые значения через пробел: ").split()
                if len(medn_enter) == 0:
                    print("\nВы не ввели никаких чисел! Попробуйте снова.\n")
                else:
                    median_list = list() 
                    errors = False
                    for i in medn_enter:
                        if isNumber(i): 
                            i = float(i)
                            median_list.append(i)
                        else:
                            print("Вы ввели не число {}. Попробуйте снова".format(i))
                            errors = True
                    if errors != True:
                        break
            print("MEDIAN == {}".format(round(median(median_list), 2))) # Расчет медианы и вывод результата с округлением до сотых
            print("Для завершения программы введите ctrl+c или ctrl+z+Enter")
    except KeyboardInterrupt:
        print("\nЗавершение программы. До новых встреч!")
    except EOFError:
        print("Завершение программы. До новых встреч! :)")
