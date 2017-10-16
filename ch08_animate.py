from microbit import *

frame1 = Image("00000:"
               "00000:"
               "00900:"
               "00000:"
               "00000:")
               
frame2 = Image("00000:"
               "09990:"
               "09090:"
               "09990:"
               "00000:")
               
frame3 = Image("99999:"
               "90009:"
               "90009:"
               "90009:"
               "99999:")

frames = [frame1, frame2, frame3, frame2]

while True:
    display.show(frames, delay=200)