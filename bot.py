import cmd
import os
import time

import CHIP_IO.GPIO as GPIO

#motors
def lhs_back_on():
    GPIO.output("GPIO2", GPIO.HIGH)
    GPIO.output("GPIO4", GPIO.HIGH)

def lhs_fwd_on():
    GPIO.output("GPIO1", GPIO.HIGH)
    GPIO.output("GPIO3", GPIO.HIGH)
    
def rhs_back_on():
    GPIO.output("GPIO5", GPIO.LOW)
    GPIO.output("GPIO7", GPIO.LOW)
    
def rhs_fwd_on():
    GPIO.output("GPIO6", GPIO.LOW)
    GPIO.output("GPIO8", GPIO.LOW)

def lhs_off():
    GPIO.output("GPIO1", GPIO.LOW)
    GPIO.output("GPIO2", GPIO.LOW)
    GPIO.output("GPIO3", GPIO.LOW)
    GPIO.output("GPIO4", GPIO.LOW)

def rhs_off():
    GPIO.output("GPIO5", GPIO.LOW)
    GPIO.output("GPIO6", GPIO.LOW)
    GPIO.output("GPIO7", GPIO.LOW)
    GPIO.output("GPIO8", GPIO.LOW)  

def all_off():
    GPIO.output("GPIO1", GPIO.LOW)
    GPIO.output("GPIO2", GPIO.LOW)
    GPIO.output("GPIO3", GPIO.LOW)
    GPIO.output("GPIO4", GPIO.LOW)

    GPIO.output("GPIO5", GPIO.LOW)
    GPIO.output("GPIO6", GPIO.LOW)
    GPIO.output("GPIO7", GPIO.LOW)
    GPIO.output("GPIO8", GPIO.LOW)

def init():
    GPIO.setup("GPIO1",GPIO.OUT)
    GPIO.setup("GPIO2", GPIO.OUT)
    GPIO.setup("GPIO4", GPIO.OUT)
    GPIO.setup("GPIO3", GPIO.OUT)

    GPIO.setup("GPIO5", GPIO.OUT)
    GPIO.setup("GPIO6", GPIO.OUT)
    GPIO.setup("GPIO7", GPIO.OUT)
    GPIO.setup("GPIO8", GPIO.OUT)

    GPIO.output("GPIO1", GPIO.LOW)
    GPIO.output("GPIO2", GPIO.LOW)
    GPIO.output("GPIO3", GPIO.LOW)
    GPIO.output("GPIO4", GPIO.LOW)

    GPIO.output("GPIO5", GPIO.LOW)
    GPIO.output("GPIO6", GPIO.LOW)
    GPIO.output("GPIO7", GPIO.LOW)
    GPIO.output("GPIO8", GPIO.LOW)


def forward(val):
    if not(val): val = 1 
    print "Going forward",val
    lhs_fwd_on()
    rhs_fwd_on()
    time.sleep(1)
    rhs_off()
    lhs_off()

def backward(val):
    if not(val): val = 1 
    print "Going backward",val

def left(val):
    if not(val): val = 1 
    print "Going left",val

def right(val):
    if not(val): val = 1 
    print "Going right",val

def speed(val):
    if not(val): val = 1 
    print "speed setting ",val

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print "hi,", person
        else:
            print 'hi'
    
    def do_fwd(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        forward(val)
    def do_f(self, line):
        """Move Forward"""
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        forward(line)

    def do_back(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        backward(val)
    def do_b(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        backward(line)

    def do_right(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        right(val)
    def do_r(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        right(line)

    def do_left(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        left(val)
    def do_l(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        left(line)
        
    def do_pause(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        left(val)
    def do_p(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        left(line)
     

    def do_speed(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        speed(line)

    def do_s(self, line):
        val =1
        if line=="":
            val=1
        else:
            val = int(line)
        speed(line)
    
    def do_quit(self, line):
        exit()
    
    def do_exit(self, line):
        exit()
    
    def postloop(self):
        print

if __name__ == '__main__':
    init()
    HelloWorld().cmdloop()
    