"""This script will go through a directory and find all files with the extension .jpg. For each file it will resize it t0 320 wide (keeping aspect ratio) (you change mywidth to whatever size you want), warm the color of the images (try and see!) and enhance the sharpness, contrast and color. Great for processsing family photos!"""

import PIL
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageOps
from PIL import Image
import os.path
import os 

mywidth = 320

for afile in os.listdir('/some/directory'):
	path = os.path.join('/some/directory', afile)
	if afile.endswith('.jpg'):
		img = PIL.Image.open(path)		
		wpercent = (mywidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		xlimg = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
		xlimg = ImageOps.crop(xlimg,border=10)
		source = xlimg.split() 
		R, G, B = 0, 1, 2
		mask = source[B].point(lambda i: i + 100)
		out = source[G].point(lambda i: i + 25)
		source[G].paste(out, None, mask)
		mask = source[B].point(lambda i: i + 100)
		out = source[R].point(lambda i: i + 35)
		source[R].paste(out, None, mask)
		xlimg = Image.merge(xlimg.mode, source)
		sharpener = ImageEnhance.Sharpness(xlimg)
		xlimg = sharpener.enhance(1)
		contraster = ImageEnhance.Contrast(xlimg)
		xlimg = contraster.enhance(1.2)
		colorizer = ImageEnhance.Color(xlimg)
		xlimg = colorizer.enhance(1.5) 
		xlimg.save('/some/directory/finals' + afile, 'JPEG', quality=75)