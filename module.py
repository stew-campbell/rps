import pyautogui
import time
import random

count = 0

while True:
    sleep = random.randint(0, 299)

    time.sleep(sleep)

    count = count + 1 * sleep

    x_coor = random.randint(859, 1059)
    y_coor = random.randint(439, 639)

    pyautogui.moveTo(x_coor, y_coor)
    pyautogui.click()

    print(x_coor, ",", y_coor)
    print(count, "sec")