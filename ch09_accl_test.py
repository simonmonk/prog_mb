from microbit import *

while True:
    x, y, z = accelerometer.get_values()
    print('x={}, y={}, z={}'.format(x, y, z))
    sleep(500)