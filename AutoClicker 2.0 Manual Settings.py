import os
import numpy as np
import pyautogui as pg
import time
from mss import mss

# Проверка файла settings.txt
if os.path.exists("settings.txt"):
    print('Файл "settings.txt" подключён')
else:
    print('Файл "settings.txt" не найден. Запустите файл "Settings Script.py"\nЗвершение работы...')
    input("Нажмите Enter для продолжения...")
    exit()

# Вывод настроек
with open('settings.txt') as fs:
    lines = fs.readlines()
Left = int(lines[0])
Top = int(lines[1])
Width = int(lines[2])
Height = int(lines[3])
R = int(lines[4])
G = int(lines[5])
B = int(lines[6])

# Захват экрана
monitor = {
        "left": Left,
        "top": Top,
        "width": Width,
        "height": Height,
}
print(monitor)
def FindColor(fcol, monitor={}):
    m = mss()
    img = m.grab(monitor)
    img_arr = np.array(img)

    #Поиск цвета (blue, green, red, alpha)
    fmap = (fcol[2], fcol[1], fcol[0], 255)
    indx = np.where(np.all(img_arr == fmap, axis=-1))
    fcrd = np.transpose(indx)
    return fcrd

# Искомый цвет
fcol = (R, G, B)
print(R, G, B)

while True:
    time1 = time.time()
    result = FindColor(fcol, monitor)
    time2 = time.time()
    if result.__len__():
        x = result[0][1]+monitor.get('left')
        y = result[0][0]+monitor.get('top')
        print(time2 - time1, [x,y])
        pg.moveTo(x,y)
    time.sleep(3)
