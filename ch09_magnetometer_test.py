from microbit import *

while True:
    z = compass.get_field_strength()
    print(z)
    sleep(500)