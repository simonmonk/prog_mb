from microbit import *

mins = 1

while True:
    if button_a.was_pressed():
        mins += 1
        if mins > 10:
            mins = 1
    display.scroll(str(mins))
 