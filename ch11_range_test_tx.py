from microbit import *
import radio

radio.on()

radio.config(power=1, data_rate=radio.RATE_250KBIT)

while True:
    radio.send("abcdefghijklmnop")
    display.show(Image.HEART, delay=100, clear=True)
    sleep(1000)