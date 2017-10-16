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
    
def save_message_index():
    with open('message_index.txt', 'w') as file:
        file.write(str(message_index))
        
def load_message_index():
    try:
        with open('message_index.txt') as file:
            contents = file.read()
        return int(contents)
    except:
        return 0
      
message_index = load_message_index()      
show_current_message()

while True:
    if button_a.was_pressed():
        message_index += 1
        if message_index >= len(messages):
            message_index = 0 
        save_message_index()
        show_current_message()