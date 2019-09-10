import cmd

def forward(val):
    print "Going forward",val

def backward(val):
    print "Going forward",val


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


    def do_quit(self, line):
        exit()
    
    def do_exit(self, line):
            exit()
    
    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
    