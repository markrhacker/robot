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
#look for face
image = cv2.imread("/Users/markhacker/Desktop/robot/cam.jpg")
cascPath = "/Users/markhacker/Desktop/robot/haarcascade_frontalface_default.xml"
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier(cascPath)

# Detect faces in the image
faces = faceCascade.detectMultiScale(gray, 1.1, 4)

print("Found {0} faces!".format(len(faces)))

##################################################
#UI
im = bimpy.Image(image)

f1 = bimpy.Float();
f2 = bimpy.Float();
f3 = bimpy.Float();

while(not ctx.should_close()):
    with ctx:
        bimpy.begin("Image")
        bimpy.image(im)
        bimpy.end()

        bimpy.begin("Analysis")
        bimpy.text("Hello, world!")

        bimpy.slider_float3("float3", f1, f2, f3, 0.0, 1.0)  

        bimpy.end()


        bimpy.begin("Console")
        bimpy.text("Image read:"+str(f1.value)+str(f2.value)+str(f3.value))
        bimpy.text("Found {0} faces!".format(len(faces)))
        bimpy.end()


