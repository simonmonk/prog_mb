from microbit import *

x = 0
l = ['a', 'b', 'c']

while True:
    if button_a.was_pressed():
        display.show(l[x])
        x += 1