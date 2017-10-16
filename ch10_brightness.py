from microbit import *

brightness = 0
step = 100

while True:
    if button_a.was_pressed() and brightness >= step:
        brightness -= step
        pin0.write_analog(brightness)
    if button_b.was_pressed() and brightness <= (1023 - step):
        brightness += step
        pin0.write_analog(brightness)
    