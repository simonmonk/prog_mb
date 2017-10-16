from microbit import *
import radio

MY_ID = 0
NUM_MICROBITS = 10

recipient = 0
radio.on()

display.show(str(MY_ID), delay=200, clear=True)
display.show(str(MY_ID), delay=200, clear=True)
display.show(str(recipient))

while True:
    if button_a.was_pressed():
        recipient += 1
        if recipient >= NUM_MICROBITS:
            recipient = 0
        display.show(str(recipient))
    if button_b.was_pressed():
        radio.send(str(recipient))
        display.show(Image.YES, delay=500, clear=True)
        display.show(str(recipient))
    try:
        message = radio.receive()
        if message and int(message) == MY_ID:
            display.show(Image.SMILE, delay=1000, clear=True)
            display.show(str(recipient))
    except:
        radio.off()
        radio.on()