from microbit import *
from math import sqrt

# Reduce to make more sensitive
MAGNET_MAX = 100000 

baseline = compass.get_z()

def scale_inv_square(a, a_max, scaled_max=5.0):
    a_max_scaled = sqrt(abs(a_max))
    a_scaled = sqrt(abs(a))
    return int(a_scaled * scaled_max / a_max_scaled)

def bargraph(a):
    display.clear()
    for y in range(0, 5):
        if a > y:
            for x in range(0, 5):
                display.set_pixel(x, 4-y, 9)
    
while True:
    z = compass.get_z()
    num_bars = scale_inv_square(z - baseline, MAGNET_MAX)
    bargraph(num_bars)
    if button_a.was_pressed():
        baseline = compass.get_z()