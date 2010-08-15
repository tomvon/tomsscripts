"""Resizes an image and keeps aspect ratio. Set mywidth to the desired with in pixels."""

import PIL
from PIL import Image

mywidth = 300

img = Image.open('afolder/someimage.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('afolder/resized.jpg')