import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import platform

# --- init everything ---
analysistype=0
ostype=0


if "Darwin" in platform.platform():
    print ("macos")
    ostype=True
else:
    print ("other")
    ostype=False


while(True):
    # --- Get image ---
    print ("Get Image...")
    if (ostype):
        os.system("ffmpeg -nostats -loglevel 0 -f avfoundation -video_size 1280x720 -framerate 30 -i \"0\" -vframes 1 cam.jpg")
    else:
        os.system("fswebcam -q cam.jpg")
    # -----------------

    #---- analysis imagee ----
    print ("Analysising...")
    #img1 = cv2.imread('box.png',0)          # queryImage
    img2 = cv2.imread('cam.jpg',0) # trainImage
    img2 = cv2.resize(img2, (256, 256)) 
    # -----------------

    # --- View image ---
    print ("Show Image...")
    #os.system("feh -g 250x250 cam.jpg ")
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',img2)
    # -----------------

    # --- Remove last image ---
    print ("Remove Image...") 
    os.system("rm cam.jpg")
    # -----------------

    # --- Exit loop keu ---
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # -----------------

# ---- clean up ----
cv2.destroyAllWindows()

