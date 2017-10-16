from microbit import *

angle = 10

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        compass.calibrate()
    heading = compass.heading()
    if heading >= (360 - angle) or heading <= angle:
        display.show("^")
        sleep(100)
    elif heading >= (180 - angle) and heading <= (180 + angle):
        display.show("V")
        sleep(100)
    else:
        display.clear()