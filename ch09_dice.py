from microbit import *
from random import randint
    
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.show(str(randint(1, 6)))