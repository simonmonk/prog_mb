from microbit import *

while True:
    pin0.write_digital(True)
    sleep(500)
    pin0.write_digital(False)
    sleep(500)
    