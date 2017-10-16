from microbit import *
from random import *

track = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

car_position = 2
delay = 500
score = 0
    
while True:
    track.set_pixel(randint(0, 4), 0, 5)
    if button_b.was_pressed() and car_position < 4:
        car_position += 1
    if button_a.was_pressed() and car_position > 0:
        car_position -= 1    
    if track.get_pixel(car_position, 4) > 0:
        display.scroll("GAME OVER!" + str(score))
        break
    track.set_pixel(car_position, 4, 9)
    display.show(track)
    track = track.shift_down(1)
    sleep(delay)
    delay -= 1
    score += 1