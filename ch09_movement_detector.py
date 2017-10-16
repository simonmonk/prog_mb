from microbit import *

THRESHOLD = 100

old_x = accelerometer.get_x()

while True:
    x = accelerometer.get_x()
    if abs(x - old_x) > THRESHOLD:
        display.scroll("ALARM!")
    old_x = x