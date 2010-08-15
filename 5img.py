"""This script is for use with Zope2. Place it in your "extensions" 
folder in your Zope instance and create an "External Method" in Zope. 
Change the "mydir" dir variable to be thepath to the directory you 
wish to store your images. 

This script will take a 4:3 proprtional image file, keywords, caption 
and source submitted from a form, resize the image into 5 sizes, 
640 x 480, 460 x 345, 300 x 255, 160 x 120 and 80x 60 and named 
with descriptive extensions (-640.jpg). These sizes have been 
chosen to work with most web page layouts based on standard ad sizes.

Images are renamed with a unique id based on the time of submission."""

def makeImages(self, imagefile, newkeywords, newcaption, newsource):

	mydir = '/my/directory/'

    import PIL.Image, ImageEnhance, ImageFilter
    import PIL
    from StringIO import StringIO
    import os.path
    import datetime
    import time

    # create the data in a new PIL Image. 
    image=PIL.Image.open(imagefile)
    image=image.convert('RGB')
    image1=image.resize((640, 480), PIL.Image.ANTIALIAS)
    image2=image.resize((460, 345), PIL.Image.ANTIALIAS)
    image3=image.resize((300, 225), PIL.Image.ANTIALIAS)
    image4=image.resize((160, 120), PIL.Image.ANTIALIAS)
    image5=image.resize((80, 60), PIL.Image.ANTIALIAS)
    image1=image.filter(ImageFilter.SHARPEN)
    image2=image2.filter(ImageFilter.SHARPEN)
    image3=image3.filter(ImageFilter.SHARPEN)
    image4=image4.filter(ImageFilter.SHARPEN)
    image5=image5.filter(ImageFilter.SHARPEN)

    # get the data in memory.
    newimage_file1=StringIO()
    image1.save(newimage_file1, "JPEG", quality=100) 
    newimage_file1.seek(0)
    newimage_file2=StringIO()
    image2.save(newimage_file2, "JPEG", quality=100) 
    newimage_file2.seek(0)
    newimage_file3=StringIO()
    image3.save(newimage_file3, "JPEG", quality=100) 
    newimage_file3.seek(0)
    newimage_file4=StringIO()
    image4.save(newimage_file4, "JPEG", quality=100) 
    newimage_file4.seek(0)
    newimage_file5=StringIO()
    image5.save(newimage_file5, "JPEG", quality=100) 
    newimage_file5.seek(0)

    # create an id for the image
    now = datetime.datetime.now()
    newimageid=now.strftime('%Y%m%d%H%M%S')
    newimage_id1=newimageid + '-640.jpg'
    newimage_id2=newimageid + '-460.jpg'
    newimage_id3=newimageid + '-300.jpg'
    newimage_id4=newimageid + '-160.jpg'
    newimage_id5=newimageid + '-80.jpg'

	path = os.path.join(mydir, newimage_id1)
	f=open(path,"wb")
	f.write(newimage_file1)
	f.close()
	
	path = os.path.join(mydir, newimage_id2)
	f=open(path,"wb")
	f.write(newimage_file2)
	f.close()
	
	path = os.path.join(mydir, newimage_id3)
	f=open(path,"wb")
	f.write(newimage_file3)
	f.close()
	
	path = os.path.join(mydir, newimage_id4)
	f=open(path,"wb")
	f.write(newimage_file4)
	f.close()
	
	path = os.path.join(mydir, newimage_id5)
	f=open(path,"wb")
	f.write(newimage_file5)
	f.close()
		
    self.REQUEST['RESPONSE'].redirect('addImageForm?msg=Image Added')