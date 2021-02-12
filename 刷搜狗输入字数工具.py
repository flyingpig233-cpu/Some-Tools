import time
import sys
import pynput.keyboard as k
import pynput.mouse as m
keyboard = k.Controller()
mouse = m.Controller()
start_point = mouse.position 
input("OK?")
while True:
    if start_point != mouse.position:
        sys.exit()
    for i in range(5):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(0.1)
    keyboard.press("2")
    keyboard.release("2")
