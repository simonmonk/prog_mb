from microbit import *

SET, RUN, ALARM = range(3)
state = SET

mins = 1
secs = 0
last_tick_time = 0

def display_mins(m):
    message = str(m)
    if m == 1:
        message += " min"
    else:
        message += " mins"
    display.scroll(message, wait=False, loop=True)
    
def display_time(m, s):
    message = str(m)
    if s < 10:
        message += ":0" + str(s)
    else:
        message += ":" + str(s)
    display.scroll(message, wait=False)

def handle_set_state():
    global state, mins
    if button_a.was_pressed():
        mins += 1
        if mins > 10:
            mins = 1
        display_mins(mins)
    if button_b.was_pressed():
        display_time(mins, secs)
        state = RUN
    
def handle_run_state():
    global state, mins, secs, last_tick_time
    if button_b.was_pressed():
        state = SET
        display_mins(mins)
    time_now = running_time()
    if time_now > last_tick_time + 5000:
        last_tick_time = time_now
        secs -= 5
        if secs < 0:
            secs = 55
            mins -= 1
        display_time(mins, secs)
    if mins == 0 and secs == 0:
        state = ALARM
        display.show(Image.HAPPY)

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