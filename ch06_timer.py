from microbit import *

SET, RUN, ALARM = range(3)
state = SET

def handle_set_state():
    
def handle_run_state():

def handle_alarm_state(): 
 
while True:
    if state == SET:
        handle_set_state()
    elif state == RUN:
        handle_run_state()
    elif state == ALARM:
        handle_alarm_state()