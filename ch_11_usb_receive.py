from microbit import *

uart.init(115200)

while True:
    if uart.any():
        message = uart.readall()
        display.scroll(message)