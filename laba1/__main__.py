import pifagor # Импорт модуля из файла

if __name__ == "__main__":
    while True:
        try:
            print("Гипотенуза.\nЧтобы выйти из программы нажмите ctrl+C или ctrl+Z+Enter")
            a = pifagor.getrnum(1)
            if a is not None:
                b = pifagor.getrnum(2)
                if b is not None:
                    if pifagor.access(a,b):
                        gip2 = pifagor.process(a, b)
                        print('\nГипотенуза равна: {:.2f}\n'.format(gip2))
        except KeyboardInterrupt: # Выход из программы сочетанием клавиш CTRL+C
            print(" ")
            print("\nЗавершение работы. \nДо новых встреч и вычислений)))")
            print(" ")
            break
        except EOFError: # Выход из программы сочетанием клавиш CTRL+Z+Enter
            print(" ")
            print("Завершение работы. \nДо новых встреч и вычислений :-)")
            print(" ")
            break