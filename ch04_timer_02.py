from microbit import *

mins = 1

def display_mins(m):
    message = str(m)
    if m == 1:
        message += " min"
    else:
        message += " mins"
    display.scroll(message)

while True:
    if button_a.was_pressed():
        mins += 1
        if mins > 10:
            mins = 1
    display_mins(mins)
 