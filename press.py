from pynput import keyboard
import os

#
# Robot controller
#

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

upprint = color.END + "UP"
downprint = color.END + "DOWN"
leftprint = color.END + "LEFT"
rightprint = color.END + "RIGHT"
f = b= l =r = False

def controller(fwd, back, left, right):

    if fwd: print "Controller: forward"
    if back: print "Controller: back"
    if left: print "Controller: left"
    if right: print "Controller: right"

    
def on_press(key):

    os.system('clear')
    upprint = color.END + "UP"
    downprint = color.END + "DOWN"
    leftprint = color.END + "LEFT"
    rightprint = color.END + "RIGHT"
    f = b= l =r = False

    try:
        if key == keyboard.Key.up:
            upprint = color.BOLD + "UP" + color.END
            f=True
        if key == keyboard.Key.down:
            downprint = color.BOLD + "DOWN" + color.END
            b=True
        if key == keyboard.Key.left:
            leftprint = color.BOLD + "LEFT" + color.END
            l=True
        if key == keyboard.Key.right:
            rightprint = color.BOLD + "RIGHT" + color.END
            r=True

        print(color.END+ upprint + '\t' + downprint+ '\t' + leftprint+ '\t' + rightprint)

        controller(f,b,l,r)
        
    except AttributeError:
        pass


def on_release(key):
    os.system('clear')
    print(color.END+ upprint + '\t' + downprint+ '\t' + leftprint+ '\t' + rightprint)

    if key == keyboard.Key.up:
            f=False
    if key == keyboard.Key.down:
            b=False
    if key == keyboard.Key.left:
            l=False
    if key == keyboard.Key.right:
            r=False
    
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



# print ("any key to start, esc to end")




    