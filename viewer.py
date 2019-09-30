#viewer.py
import bimpy
from PIL import Image

#################################################
#init
ctx = bimpy.Context()
ctx.init(800, 800, "Image")

#################################################
#get image




##################################################
#view image
image = Image.open("cam.jpg")

im = bimpy.Image(image)

while(not ctx.should_close()):
    with ctx:
        bimpy.text("Display PIL Image")

        bimpy.image(im)

