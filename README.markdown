
A few useful python scripts I wrote for various reasons. Enjoy!

Tom Von Lahndorff http://www.tomvl.com http://www.modscape.com

***

###5img.py###

This script is for use with Zope2. Place it in your "extensions" folder in your Zope instance and create an "External Method" in Zope. Change the "mydir" dir variable to be the path to the directory you wish to store your images. 

This script will take a 4:3 proprtional image file, keywords, caption and source submitted from a form, resize the image into 5 sizes, 640 x 480, 460 x 345, 300 x 255, 160 x 120 and 80 x 60 and named with descriptive extensions (-640.jpg). These sizes have been chosen to work with most web page layouts based on standard ad sizes.

Images are renamed with a unique id based on the time of submission.

***

###cleanID.py###

This script will remove "nasty" characters from a string. Useful for sanitizing file ids.

***

###getEmails.py###

This script retrieves email from a mailserver and looks for image atttachments. If any are found it uses PIL (requires PIL obviously) to resize them into 3 sizes. It returns a list of emails with subject, images and the body of the email (text). I used this script to be able blog by email to custom Zope2 blog app. The PIX-FLIX line is in there because fscking Verizon would automatically add it any emails sent from my phone and there was no way to remove it.

***

###img_resizer.py###

Resizes an image and keeps aspect ratio. Set mywidth to the desired with in pixels.

***

###img_warmfilter.py###

This script will go through a directory and find all files with the extension .jpg. For each file it will resize it t0 320 wide (keeping aspect ratio) (you change mywidth to whatever size you want), warm the color of the images (try and see!) and enhance the sharpness, contrast and color. Great for processsing family photos!

