from microbit import *
import radio

x = 0
radio.on()

while True:
    if button_a.was_pressed():
        radio.send(str(x))
        x += 1