from microbit import *

SET, RUN, ALARM = range(3)
state = SET

def handle_set_state():
    global state
    display.show("S")
    if button_b.was_pressed():
        state = RUN
    
def handle_run_state():
    global state
    display.show("R")
    if button_b.was_pressed():
        state = SET

def handle_alarm_state(): 
    pass
 
while True:
    if state == SET:
        handle_set_state()
    elif state == RUN:
        handle_run_state()
    elif state == ALARM:
        handle_alarm_state()