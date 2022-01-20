import os
Count = 0
print("1. Настройка AutoCliker 1.0\n2. Настройка AutoCliker 2.0\n3. Справка\n4. Выход")
text = int(input("Введите число: "))
Count = text

if Count == 1:
    print("\nЭта функция будет доступна в следующем обновлении")
    input("Нажмите Enter для продолжения...")
    exit()

while Count == 2:
    if os.path.exists("settings.txt"):
        Count1 = 0
        print('Файл "settings.txt" был найден.\n1. Перезаписать файл настроек\n2. Выход')
        ftxt = int(input("Введите число: "))
        if ftxt == 1:
            os.remove("settings.txt")
        else:
            exit()
    else:
        print('Файл "settings.txt" не найден')
        sett_file = open("settings.txt", "w+")
        print("\n          ------------Настройка области захвата-----------\n\n------------Настройка левой верхней точки области захвата-----------\n")

        Left = int(input("Введите отступ(в пикселях) от верхней части "))
        sett_file.write(str(Left))
        sett_file.write("\n")
        Top = int(input("Введите отступ(в пикселях) от левой части экрана "))
        sett_file.write(str(Top))
        sett_file.write("\n")
        print("\n ------------Настройка ширины и высоты области захвата------------\n2")
        Width = int(input("Ширина области "))
        sett_file.write(str(Width))
        sett_file.write("\n")
        Height = int(input("Высота области "))
        sett_file.write(str(Height))
        sett_file.write("\n")

        print("\n         ------------Настройка поиска цвета------------\n")
        print('Цвет настраивается в цветовом пространстве RGB.Узнайте "координаты" цвета в фоторедакторе')
        R = int(input("Красный "))
        sett_file.write(str(R))
        sett_file.write("\n")
        G = int(input("Зелёный "))
        sett_file.write(str(G))
        sett_file.write("\n")
        B = int(input("Синий "))
        sett_file.write(str(B))
        sett_file.write("\n")
        print("\nНастройка завершена")
        input("Нажмите Enter для продолжения...")
        exit()


if Count == 3:
    print("AutoClikerColor - сборник скриптов, автоматизирующих управление мышкой. На данный момент доступна версия скрипта 2.0\n\n")
    print("AutoCliker 1.0\nСкрипт находиться в разработке, настройка недоступна\n\n")
    print("AutoCliker 2.0\nПоддерживает поиск только одного цвета, Сначала настраивается левая верхняя точка области захвата, затем ширина и высота области,\nпосле указываются координаты цвета, по которому будет наводиться мышь")
    exit()


if Count == 4:
    exit()

else:
    exit()
