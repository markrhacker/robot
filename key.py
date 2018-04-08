'''
geek order
male cables
female cables
8 off relays
distance sensor
breadboard
HDMI switch


'''

import curses
import os

keys = []

for i in range (1,100):
    keys.append(False)



def main(win):
    win.nodelay(False)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:

        try:
            keyup=False
            keydown=False
            keyleft=False
            keyright=False
            key = win.getkey()
            win.clear()
            win.refresh()
            win.addstr("Detected key:")

            if key == str("KEY_UP"):
                keyup=True
                win.addstr(str(key))

            if key == str("KEY_DOWN"):
                keydown=True
                win.addstr(str(key))

            if key == str("KEY_LEFT"):
                keyleft=True
                win.addstr(str(key))

            if key == str("KEY_RIGHT"):
                keyright=True
                win.addstr(str(key))

            if key == os.linesep:
                win.addstr(" ")
                break

        except Exception as e:
           pass

curses.wrapper(main)
