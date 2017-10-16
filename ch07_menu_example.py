from microbit import *
from menu import *
            
image_menu = Menu({"Happy" : Image.HAPPY, "Sad" : Image.SAD, "Angry" : Image.ANGRY})

while True:
    answer = image_menu.ask()
    display.show(answer)
    sleep(5000)

