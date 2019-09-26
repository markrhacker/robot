import cmd
import os
import time
from pathlib import Path

import CHIP_IO.GPIO as GPIO


#################################################################
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#################################################################

global STEPTIME
STEPTIME = 1

#motors
def lhs_back_on():
    GPIO.output("GPIO1", GPIO.LOW)
    GPIO.output("GPIO2", GPIO.LOW)
    GPIO.output("GPIO3", GPIO.LOW)

def lhs_fwd_on():
    GPIO.output("GPIO3", GPIO.LOW)
    
def rhs_back_on():
    GPIO.output("GPIO4", GPIO.LOW)
    GPIO.output("GPIO5", GPIO.LOW)
    GPIO.output("GPIO6", GPIO.LOW)
 
def rhs_fwd_on():
    GPIO.output("GPIO6", GPIO.LOW)

def lhs_off():
    GPIO.output("GPIO1", GPIO.HIGH)
    GPIO.output("GPIO2", GPIO.HIGH)
    GPIO.output("GPIO3", GPIO.HIGH)

def rhs_off():
    GPIO.output("GPIO4", GPIO.HIGH)
    GPIO.output("GPIO5", GPIO.HIGH)
    GPIO.output("GPIO6", GPIO.HIGH)

def all_off():
    GPIO.output("GPIO1", GPIO.LOW)
    GPIO.output("GPIO2", GPIO.LOW)
    GPIO.output("GPIO3", GPIO.LOW)
    GPIO.output("GPIO4", GPIO.LOW)
    GPIO.output("GPIO5", GPIO.LOW)
    GPIO.output("GPIO6", GPIO.LOW)

def init():
    GPIO.setup("GPIO1", GPIO.OUT)
    GPIO.setup("GPIO2", GPIO.OUT)
    GPIO.setup("GPIO4", GPIO.OUT)
    GPIO.setup("GPIO3", GPIO.OUT)
    GPIO.setup("GPIO5", GPIO.OUT)
    GPIO.setup("GPIO6", GPIO.OUT)


    GPIO.output("GPIO1", GPIO.HIGH)
    GPIO.output("GPIO2", GPIO.HIGH)
    GPIO.output("GPIO3", GPIO.HIGH)
    GPIO.output("GPIO4", GPIO.HIGH)
    GPIO.output("GPIO5", GPIO.HIGH)
    GPIO.output("GPIO6", GPIO.HIGH)



def forward(val):
    if not(val): val = 1.0 
    print "Going forward",val
    lhs_fwd_on()
    rhs_fwd_on()
    print STEPTIME, val
    time.sleep(STEPTIME*float(val))
    lhs_off()
    rhs_off()

def backward(val):
    if not(val): val = 1.0 
    print "Going backward",val
    lhs_back_on()
    rhs_back_on()
    time.sleep(STEPTIME*val)
    lhs_off()
    rhs_off()

def left(val):
    if not(val): val = 1.0 
    print "Going left",val
    lhs_back_on()
    rhs_fwd_on()
    time.sleep(STEPTIME*val)
    lhs_off()
    rhs_off()

def right(val):
    if not(val): val = 1 
    print "Going right",val
    lhs_fwd_on()
    rhs_back_on()
    time.sleep(STEPTIME*val)
    lhs_off()
    rhs_off()

def speed(val):
    if not(val): val = 1 
    print "speed setting ",val

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_fwd(self, line):
        """Move Forward"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        forward(val)
    def do_f(self, line):
        """Move Forward"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        forward(line)

    def do_back(self, line):
        """Move back"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        backward(val)
    def do_b(self, line):
        """Move back"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        backward(line)

    def do_right(self, line):
        """Move right"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        right(val)
    def do_r(self, line):
        """Move right"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        right(line)

    def do_left(self, line):
        """Move left"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        left(val)
    def do_l(self, line):
        """Move left"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        left(line)
        
    def do_pause(self, line):
        """MPause"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        #left(val)

    def do_p(self, line):
        """Pause"""
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        #left(line)
     

    def do_step(self, line):
        """Change step"""
        global STEPTIME
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        STEPTIME=val

    def do_s(self, line):
        """Change step"""
        global STEPTIME
        val =1
        if line=="":
            val=1
        else:
            val = float(line)
        STEPTIME=val
        
    

    def do_script(self, line):
        """script"""
        print "executing script"
        my_file = Path(line)
        if my_file.is_file():
            print(bcolors.OKGREEN+"Running script"+ bcolors.ENDC)
        else:
            print(bcolors.WARNING+"File not found"+ bcolors.ENDC)
            return
        with open(line) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def do_quit(self, line):
        """exit"""
        exit()
    
    def do_exit(self, line):
        """exit"""
        exit()
    
    def postloop(self):
        print

if __name__ == '__main__':
    init()
    HelloWorld().cmdloop()
    