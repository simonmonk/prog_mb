from microbit import *
from random import randint

display.clear()

while True:
    x = randint(0, 4)
    y = randint(0, 4)
    brightness = randint(0, 1)
    display.set_pixel(x, y, brightness * 9)
    sleep(50)