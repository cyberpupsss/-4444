import math
def t1():
    print('Расчет вклада')

    while True:
        try:
            p = float(input("Введите процентную ставку p (0 < p < 25): "))
            if 0 < p < 25:
                break
            else:
                print("Ошибка: p должно быть в диапазоне (0; 25)")
        except:
            print("Ошибка: введите вещественное число")

    bank = 1000
    count = 0
    while bank <= 1100:
        bank += bank*(p/100)
        count += 1

    print(f"Через {count} месяцев размер вклада превысит 1100 руб")
    print(f"Итоговый размер вклада составляет: {bank} руб")



def t2():
    print('Табулирование функции')

    while True:
        try:
            x0 = float(input("Введите конец отрезка х0: "))
            break
        except:
            print("Ошибка: Введите число")

    while True:
        try:
            x1 = float(input("Введите конец отрезка х1: "))
            if x1>=x0:
                break
            else:
                print("Ошибка: х1 должен быть больше или равен х0 ")
        except:
            print("Ошибка: Введите число")

    while True:
        try:
            dx = float(input("Введите шаг dx:"))
            if dx > 0:
                break
            else:
                print("Ошибка: шаг не может быть отрицательным ")
        except:
            print("Ошибка: Введите число")


    x = x0
    while x <= x1:
        if x < 0:
            z = x ** 2
        elif 0 < x <= 1:
            z = math.sin(x)
        else:
            z = math.cos(x)

        print(f"{x}\t{z}")
        x += dx



def t3():
    print('Вывод цифр числа')

    while True:
        try:
            n = int(input("Введите целое число n > 0): "))
            if n > 0:
                break
            else:
                print("Ошибка: n должно быть больше 0")
        except:
            print("Ошибка: введите целое число")

    print("Цифры числа, начиная с младшего разряда:")


    if n == 0:
        print(0)
    else:
        while n > 0:
            res = n % 10
            print(res)
            n = n // 10



while True:
    print('Выберите задание:')
    print('1 - Расчет вклада')
    print('2 - Табулирование функции')
    print('3 - Вывод цифр числа')
    print('0 - Выход')

    c = input('Введите номер задания:')

    if c == '1':
        t1()
    elif c == '2':
        t2()
    elif c == '3':
        t3()
    elif c == '0':
        print('Всего доброго, пользователь <3')
        break




