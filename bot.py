import cmd
import os
try:
    import CHIP_IO.GPIO as GPIO
except ImportError:
    print "Needs to run on the CHIP"

def forward(val):
    if not(val): val = 1 
    print "Going forward",val

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
    HelloWorld().cmdloop()
    