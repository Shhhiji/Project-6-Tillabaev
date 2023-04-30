
def schet(num_list): # Функция отвечающая за счет среднего значения
    sum_num = 0
    for x in num_list:
        sum_num = sum_num + x
    avg = sum_num / len(num_list)
    return avg

# Обработать числа с запятой

def mean_avg():
    try:
        while True:
            while True:
                averg_str = input("Подсчет среднего значения.\nВведите числовые значения через пробел: ").split()
                if len(averg_str) == 0:
                    print("Вы не ввели никаких чисел! Попробуйте снова.")
                else:
                    averg = list()
                    haserrors = False
                    for i in averg_str:
                        if i.isnumeric(): # Вызов встроенно функии для проверки ввода, ввел пользователь число или нет
                            i = float(i)
                            averg.append(i)
                        else:
                            print("Вы ввели не число {}. Попробуйте снова".format(i))
                            haserrors = True
                    if haserrors != True:
                        break

            print(round(schet(averg), 2)) # Вывод результата с округлением до сотых
            print("Для завершения программы введите ctrl+c или ctrl+z+Enter")
    except KeyboardInterrupt:
        print("Завершение программы. До новых встреч!")
    except EOFError:
        print("Завершение программы. До новых встреч!))")
        




