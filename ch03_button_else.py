from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll("Please don't press this button again")
    else:
        display.scroll("Press button A")