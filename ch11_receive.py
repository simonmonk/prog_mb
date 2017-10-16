from microbit import *
import radio

radio.on()

while True:
    try:
        message = radio.receive()
        if message:
            display.show(message)
    except:
        radio.off()
        radio.on()