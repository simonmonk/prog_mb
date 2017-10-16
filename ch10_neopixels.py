from microbit import *
from neopixel import NeoPixel

num_pixels = 8
color = [255, 0, 255] # red, green, blue
off = [0, 0, 0]

pixels = NeoPixel(pin0, num_pixels)

while True:
    for i in range(0, num_pixels):
        pixels[i] = color
        pixels.show()
        sleep(100)
        pixels[i] = off
        pixels.show()