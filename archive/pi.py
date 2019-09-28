# import the pygame module, so you can use it
import pygame
from pygame.locals import *
import os

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


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

#   logo = pygame.image.load("logo32x32.png")
#    pygame.display.set_icon(logo)
#    pygame.display.set_caption("minimal program")
#    screen = pygame.display.set_mode((240,180))


    # define a variable to control the main loop
    running = True
    x = 20
    y = 20
    upprint = color.END + "UP"
    downprint = color.END + "DOWN"
    leftprint = color.END + "LEFT"
    rightprint = color.END + "RIGHT"


    # main loop
    while running:

        upprint = color.END + "UP"
        downprint = color.END + "DOWN"
        leftprint = color.END + "LEFT"
        rightprint = color.END + "RIGHT"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 1
            upprint = color.BOLD + "UP" + color.END

        if keys[pygame.K_DOWN]:
            y += 1
            downprint = color.BOLD + "DOWN" + color.END

        if keys[pygame.K_LEFT]:
            x -= 1
            leftprint = color.BOLD + "LEFT" + color.END

        if keys[pygame.K_RIGHT]:
            x += 1
            rightprint = color.BOLD + "RIGHT" + color.END

        if keys[pygame.K_ESCAPE]:
            running = False

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        os.system('clear')
        print(x, y)
        print(color.END+ upprint + '\t' + downprint+ '\t' + leftprint+ '\t' + rightprint)


if __name__=="__main__":
    # call the main function
    main()
