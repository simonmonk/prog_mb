from microbit import *
import radio

radio.on()

radio.config(power=1, data_rate=radio.RATE_250KBIT)

while True:
    message = radio.receive()
    if message and message == "abcdefghijklmnop":
        display.show(Image.YES, delay=100, clear=True)
    