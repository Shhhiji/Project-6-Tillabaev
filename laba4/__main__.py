import triangle # Импорт модуля из файла
from error import getrnum # Импорт модуля возможно возникших ошибок из файла

if __name__ == "__main__":
    while True:
        try:
            print("Это точно треугольник?\n")
            a = getrnum(1)
            if a is not None:
                b = getrnum(2)
                if b is not None:
                    c = getrnum(3)
                    if c is not None:
                        if triangle.access(a, b, c):
                            triangle.check(a, b, c)
        except KeyboardInterrupt: # Выход из программы сочетанием клавиш CTRL+C
            print("\nЗавершение работы. \nДо новых встреч и вычислений)))")
            break
        except EOFError: # Выход из программы сочетанием клавиш CTRL+Z+Enter
            print("Завершение работы. \nДо новых встреч и вычислений :)")
            break
        print("\nЧтобы выйти из программы нажмите ctrl+c или ctrl+z+Enter\n")