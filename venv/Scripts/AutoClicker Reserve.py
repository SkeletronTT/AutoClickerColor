import numpy as np
import pyautogui as pg
import time
from mss import mss

# Захват экрана
monitor = {
        "left": 1154,
        "top": 285,
        "width": 361,
        "height": 478,
}
def FindColor(fcol, monitor={}):
    #85 172 238
    m = mss()
    img = m.grab(monitor)
    img_arr = np.array(img)

    #Поиск цвета (b, g, r, a)
    fmap = (fcol[2], fcol[1], fcol[0], 255)
    indx = np.where(np.all(img_arr == fmap, axis=-1))
    fcrd = np.transpose(indx)
    return fcrd

#Искомый цвет
fcol = (224, 67, 167)

while True:
    time1 = time.time()
    result = FindColor(fcol, monitor)
    time2 = time.time()
    if result.__len__():
        x = result[0][1]+monitor.get('left')
        y = result[0][0]+monitor.get('top')
        print(time2 - time1, [x,y])
        pg.moveTo(x,y)
        pg.moveRel(3, 3)
        pg.click()
    time.sleep(0.1)
