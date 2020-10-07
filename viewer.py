#viewer.py
import bimpy
import os
from PIL import Image
import cv2
import numpy
import socket
import time
import math


#################################################\
#init
ctx = bimpy.Context()
ctx.init(700, 800, "Image")

#################################################
#get image

#Webcam
#MacOS
#brew install 
#imagesnap -w 2 cam.jpg
#LINUX
#sudo apt-get install fswebcam
#fswebcam -r 1280x1024 --line-colour '#FF000000' --banner-colour '#FF000000' -F 10 cam.jpg

#remote

#local
#pil_image = Image.open("/Users/markhacker/Desktop/robot/cam.jpg")
#pil_image = pil_image.resize((640,350), Image.ANTIALIAS)
#opencvImage = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
##################################################
#look for face

def WebCamInit():
    print("Warming up cam")

def TakeWebCamIamge():
    print("click!")
    os.system("imagesnap -w 2 /Users/markhacker/Desktop/robot/cam.jpg")

def getCamImage():
    image = cv2.imread("/Users/markhacker/Desktop/robot/cam.jpg")
    height, width = image.shape[:2]
    width = int(width/1.4)
    height = int(height/1.4)
    image = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
    return image, width, height

def DetectFace(image):
    cascPath = "/Users/markhacker/Desktop/robot/haarcascade_frontalface_default.xml"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    print("Found {0} faces!".format(len(faces)))

    return faces

def DrawFaces(image,faces):
    #HACK FIND LARGED w x h face
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        facestr= str(x)+' '+str(y)+' '+str(w)+' '+str(h)
        lineThickness = 1
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), lineThickness)
        x1 = int(x+(w/2))
        y1 = y 
        x2 = int(x+(w/2))
        y2 = int(y+h)
        cv2.line(image, (x1, y1), (x2, y2), (255,0,0), lineThickness)
        x1 = x
        y1 = int(y+h/2)
        x2 = int(x+w)
        y2 = int(y+h/2)
        cv2.line(image, (x1, y1), (x2, y2), (255,0,0), lineThickness)   
        headx = int(x+w/2)
        heady = int(y+h/2)

        return facestr,headx,heady

def DrawHUD(image,width,height,headx,heady):
    #hud
    lineThickness = 6
    x1 = int(width/2)
    y1 = 0 
    x2 = int(width/2)
    y2 = int(height)
    cv2.line(image, (x1, y1), (x2, y2), (0,255,0), lineThickness)
    x1 = 0
    y1 = int(height/2)
    x2 = int(width)
    y2 = int(height/2)
    cv2.line(image, (x1, y1), (x2, y2), (0,255,0), lineThickness)
    camx = int(width/2)
    camy = int(height/2)

    #vector
    x1 = camx
    y1 = camy
    x2 = headx
    y2 = heady
    cv2.arrowedLine(image, (x1, y1), (x2, y2), (0,0,255), lineThickness)

    dirvecx = camx - headx
    dirvecy = camy - heady
    dirvecxnorm = dirvecx/width
    dirvecynorm = dirvecy/height
    print(dirvecx,dirvecy,dirvecxnorm,dirvecynorm)
    dirvecmag = math.sqrt(abs(dirvecx)*abs(dirvecx)+abs(dirvecy)+abs(dirvecy))/math.sqrt(width*width+height+height)
    dirvecmagnorm = math.sqrt(abs(dirvecx)*abs(dirvecx)+abs(dirvecy)+abs(dirvecy))
    return dirvecx,dirvecy,dirvecxnorm,dirvecynorm,dirvecmag,dirvecmagnorm


WebCamInit()
TakeWebCamIamge()
image, width, height = getCamImage()
dirvecx = 0
dirvecy =0
dirvecxnorm=0
dirvecynorm=0
dirvecmag=0
dirvecmagnorm=0

#if (dirvecx<0):
        
##################################################
#UI
im = bimpy.Image(image)

f1 = bimpy.Float();
f2 = bimpy.Float();
f3 = bimpy.Float();

facestr =""

while(not ctx.should_close()):
    with ctx:
        TakeWebCamIamge()
        image, width, height = getCamImage()
        faces = DetectFace(image)
        if (len(faces)>0):
            facestr,headx,heady = DrawFaces(image,faces)
            dirvecx,dirvecy,dirvecxnorm,dirvecynorm,dirvecmag,dirvecmagnorm=DrawHUD(image,width,height,headx,heady)

        im = bimpy.Image(image)
        bimpy.begin("Image")
        bimpy.image(im)
        bimpy.end()

        bimpy.begin("Analysis")
        bimpy.text("Hello, world!")

        f1.value = abs(dirvecxnorm)
        f2.value = abs(dirvecynorm)
        f3.value = abs(dirvecmag)

        bimpy.slider_float3("Face Vector", f1, f2, f3, 0.0, 1.0)  

        bimpy.end()

        bimpy.begin("Console")
        bimpy.text("Image read:"+str(f1.value)+str(f2.value)+str(f3.value))
        bimpy.text("Found {0} faces!".format(len(faces)))
        bimpy.text(facestr)
        bimpy.text("Direction vector:"+str(dirvecx)+' '+str(dirvecy)+' '+str(dirvecmag))

        #for (x, y, w, h) in faces:
        
            #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        bimpy.end()


