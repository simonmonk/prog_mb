from microbit import *

mins = 1

def pluralize(word, x):
    if x == 1:
        return word
    else:
        return word + "s"

def display_mins(m):
    display.scroll(str(m) + pluralize("min", m))

while True:
    if button_a.was_pressed():
        mins += 1
        if mins > 10:
            mins = 1
    display_mins(mins)