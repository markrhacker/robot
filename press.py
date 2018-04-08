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

f = b= l =r = False
upprint = color.END + "UP"
downprint = color.END + "DOWN"
leftprint = color.END + "LEFT"
rightprint = color.END + "RIGHT"
speedprint = color.END + "FAST"

m1p = m2p = m1n = m2n =sp1 = sp2 =sp3 = False
m1pprint = " - " 
m2pprint = " - "
m1nprint = " - "
m2nprint = " - "
sp1print = " - "
sp2print = " - "
sp3print = " - "

#
# ---- Set the GPIP based on controller logic and key input
def setgpio(gpio1,gpio2,gpio3,gpio4,gpio5,gpio6,gpio7 ):
    print "GPIO"

#
# --- Controller logic based on key input ---
def controller(fwd, back, left, right):
    m1p = m2p = m1n = m2n =sp1 = sp2 =sp3 = False
    m1pprint = " - " 
    m2pprint = " - "
    m1nprint = " - "
    m2nprint = " - "
    sp1print = " - "
    sp2print = " - "
    sp3print = " - "

# controller logic
    if fwd:
        #print "Controller: forward"
        m1p = True
        m1pprint = " X "
        m2p = True
        m2pprint = " X "
        sp3 = True
        sp3print = " X "

    if back:
        #print "Controller: back"
        m1n = True
        m1nprint = " X "
        m2n = True
        m2nprint = " X "
        sp3 = True
        sp3print = " X "       

    if left: 
        #print "Controller: left"
        m1p = True
        m1pprint = " X "
        m2n = True
        m2nprint = " X "
        sp3 = True
        sp3print = " X "

    if right: 
        #print "Controller: right"
        m1n = True
        m1nprint = " X "
        m2p = True
        m2pprint = " X "
        sp3 = True
        sp3print = " X "


    setgpio(m1p, m1n, m2p, m2n, sp1, sp2, sp3)
    print "===========GPIO============"
    print "M1+ M1- M2+ M2- SP1 SP2 SP3"
    print m1pprint +" "+ m1nprint +" "+ m2pprint +" "+ m2nprint +" "+ sp1print +" "+ sp2print +" "+ sp3print
    #print " X   -   X   -   X   -   - "
    
    
def on_press(key):

    os.system('clear')
    upprint = color.END + "UP"
    downprint = color.END + "DOWN"
    leftprint = color.END + "LEFT"
    rightprint = color.END + "RIGHT"
    f = b= l =r = False
    speed = 3
    
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

    f = b= l =r = False
    os.system('clear')
 
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

    print(color.END+ upprint + '\t' + downprint+ '\t' + leftprint+ '\t' + rightprint)
    controller(f,b,l,r)

def main():
    # Collect events until released
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
            listener.join()                


if __name__ == "__main__":
    # execute only if run as a script
    print "Must be run as root"
    print "Any key to start, esc to end"
    main()

    
    
# print ("any key to start, esc to end")


