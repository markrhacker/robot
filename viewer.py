#viewer.py
import bimpy
import os
from PIL import Image
import cv2

#################################################\
#init
ctx = bimpy.Context()
ctx.init(700, 800, "Image")

#################################################
#get image
image = Image.open("/Users/markhacker/Desktop/robot/cam.jpg")
image = image.resize((640,350), Image.ANTIALIAS)
#MacOS
#brew install 
#imagesnap -w 2 cam.jpg
#Linux
#sudo apt-get install fswebcam
#fswebcam -r 1280x1024 --line-colour '#FF000000' --banner-colour '#FF000000' -F 10 cam.jpg

##################################################
#view image


im = bimpy.Image(image)

while(not ctx.should_close()):
    with ctx:
        bimpy.begin("Image")
        bimpy.image(im)
        bimpy.end()

        bimpy.begin("Analysis")
        bimpy.text("Hello, world!")
        bimpy.end()


        bimpy.begin("Console")
        bimpy.text("Image read")
        bimpy.end()


