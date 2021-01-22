import math


def qadsta (a, b, c):
    """ЩИТАЕМ КВАДРАТНОЕ УРАВНЕНИЕ"""
    d = int(b**2 - 4*a*c)
    if d < 0:
        print("D < 0")
    elif d == 0:
        otvet = "X = " + str(-b / 2*a)
        return otvet
    else:
        otvet1 = "X1 = " + str(((-b + math.sqrt(d)) / (2*a)))
        otvet2 = "X2 = " + str(((-b - math.sqrt(d)) / (2*a)))
        return otvet1, otvet2


def asking():
    """СПРАШИВАЕМ ПОЛЬЗОВАТЕЛЯ ЧЁ ОН ХОЧЕТ"""
    inputwords_quadrat_array = ["q", "qua", "quadrat", "квадратные", "кв", "квадрат", "4", "qu", "kv", "к"]
    stop = ["Stop", "stop", "s", "STOP"]
    inputwords = ""
    print("[stop] for finsh programm")
    print("=========================")
    while True:
        inputwords = input(" Kakie    Yravnenia? | ")
        if inputwords in inputwords_quadrat_array:
            a = int(input("Vvidite chislo A: "))
            b = int(input("Vvidite chislo B: "))
            c = int(input("Vvidite chislo C: "))
            print("______________________Reshaem____________________________")
            print("D = " + str(b) + " * 2 - 4 * " + str(a) + " * " + str(c))
            print(qadsta(a, b, c))
        elif inputwords in stop:
            break
        else:
            print("___________________Fignu napechatal______________________")


# ____________________MAIN________________________

asking()
