from microbit import *

messages = [
    "-",
    "I've gone out",
    "Do not disturb",
    "I'm at the shops, message me if you can think of anything we need",
    "I'm in the garden",
    "Give me a call",
    "I'm in the bath, a cup of tea would be nice"
]

message_index = 0

def show_current_message():
    display.scroll(messages[message_index], wait=False, loop=True)

show_current_message()

while True:
    if button_a.was_pressed():
        message_index += 1
        if message_index >= len(messages):
            message_index = 0 
        show_current_message()