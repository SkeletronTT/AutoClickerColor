import numpy as np
import pyautogui as pg
import time
from mss import mss

# Вывод настроек
with open('settings.txt') as fs:
    lines = fs.readlines()
Left = lines[6]
Top = lines[7]
Width = lines[11]
Height = lines[12]
R = lines[17]
G = lines[18]
B = lines[19]

# Захват экрана
monitor = {
        "left": Left,
        "top": Top,
        "width": Width,
        "height": Height,
}
print(monitor)
def FindColor(fcol, monitor={}):
    #85 172 238
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
