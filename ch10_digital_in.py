from microbit import *

while True:
    if pin0.read_digital():
        display.show(Image.YES)
    else:
        display.show(Image.NO)