from microbit import *

SET, RUN, ALARM = range(3)
state = SET

mins = 1

def display_mins(m):
    message = str(m)
    if m == 1:
        message += " min"
    else:
        message += " mins"
    display.scroll(message, wait=False, loop=True)

def handle_set_state():
    global state, mins
    if button_a.was_pressed():
        mins += 1
        if mins > 10:
            mins = 1
        display_mins(mins)
    if button_b.was_pressed():
        state = RUN
    
def handle_run_state():
    global state
    display.show("R")
    if button_b.was_pressed():
        state = SET
        display_mins(mins)

def handle_alarm_state(): 
    pass
 
display_mins(mins)
 
while True:
    if state == SET:
        handle_set_state()
    elif state == RUN:
        handle_run_state()
    elif state == ALARM:
        handle_alarm_state()