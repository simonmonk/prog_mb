from microbit import *
    
while True:
    reading = pin0.read_analog() # 0 to 1023
    voltage = reading * 3.16 / 1023
    display.show("{:.1f}".format(voltage))