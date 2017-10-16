from microbit import *

while not button_a.was_pressed():
    display.scroll("Press A")
    
display.scroll("Terminating!")
    