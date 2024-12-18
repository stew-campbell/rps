import pyautogui
import time
import random

# global variable
count = 0

# main loop generates a randome number between 0 and 299 (5 min) and assigns that value to the sleep variable
# the time.sleep function then pauses the main loop for that random value (somewhere between 0 and 299 seconds)
# the count variable increments every time the loop is run and adds the sleep time
# assign values to x_coor and y_coor variables that randomly select a point on screen within certain bounds
# move the mouse and clock at that selected point
# print the coordinates and count as a time in the terminal

# main loop
while True:
    # generate a random number between 0, 299 (5 min)
    sleep = random.randint(0, 299)

    # use sleep variable to randomize time between clicks
    time.sleep(sleep)

    #increment time by time between clicks
    count = count + 1 * sleep

    x_coor = random.randint(859, 1059)
    y_coor = random.randint(439, 639)

    pyautogui.moveTo(x_coor, y_coor)
    pyautogui.click()

    print(x_coor, ",", y_coor)
    print(count, "sec")