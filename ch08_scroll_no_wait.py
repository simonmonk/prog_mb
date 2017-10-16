from microbit import *

display.scroll("Press A to start")

while True:
    if button_a.was_pressed():
        display.scroll("Press B to stop", wait=False, loop=True)
    if button_b.was_pressed():
        display.clear()
