import Heron # Импорт модуля из файла
import error

if __name__ == "__main__":
    while True:
        try:
            print("Треугольник ли?\nФормула Герона")
            a = error.getnum(1)
            if a is not None:
                b = error.getnum(2)
                if b is not None:
                    c = error.getnum(3)
                    if c is not None:
                        if Heron.access(a, b, c):
                            if Heron.check(a, b, c):   
                                area_triangle = Heron.process(a, b, c)
                                if area_triangle is not False:
                                    print("\nВаша площадь треугольника равна: {:.2f}".format(area_triangle))
                                    print("\nДля завершениия работы программы можете нажать ctrl+c или ctrl+z+Enter\n")
        except KeyboardInterrupt: # Выход из программы сочетанием клавиш ctrl+c
            print(" ")
            print("\nЗавершение работы. \nДо новых встреч и вычислений)))")
            print(" ")
            break
        except EOFError: # Выход из программы сочетанием клавиш ctrl+z+Enter
            print(" ")
            print("Завершение работы. \nДо новых встреч и вычислений :-)")
            print(" ")
            break