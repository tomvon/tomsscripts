"""This script retrieves email from a mailserver and looks for image atttachments.
If any are found it uses PIL (requires PIL obviously) to resize them into 3 sizes. 
It returns a list of emails with subject, images and the body of the email (text). 
I used this script to be able blog by email to custom Zope2 blog app. The PIX-FLIX 
line is in there because fscking Verizon would automatically add it any emails sent 
from my phone and there was no way to remove it."""

def getEmail():
	
	import PIL
	from PIL import ImageEnhance
	from PIL import ImageFilter
	from PIL import Image
	from StringIO import StringIO
	import email
	import poplib
	import os.path
	import datetime
	import string
	import random
	
	server = poplib.POP3("mail.server.com")
	print server.getwelcome()
	print server.user("username")
	print server.pass_("password")
	
	nummsg = len(server.list()[1])
	
	names = []
	subjs = []
	bodys = []
	msgn = 1
	while msgn <= nummsg:
		smsg = server.retr(msgn)[1]
		msg = email.message_from_string('\n'.join(smsg))
		if msg.is_multipart():
			imgnames = []
			for data in msg.walk():
				name=data.get_param('name')
				if name != None and name.endswith('.jpg'):
					now = datetime.datetime.now()
					rand = random.randint(1,100000)
					iid = now.strftime('%y%j%H%m%s') + str(rand)
					#name = now.strftime('%y%j%H%m%s') + str(rand) + '.jpg'
					#iid = string.replace(name,'.jpg','') + '_' + str(msgn)
					#iid = iid[0:25]
					path = os.path.join('/path/to/your/static/images/', iid)
					f=open(path,"wb")
					f.write(data.get_payload(decode=1))
					f.close()
					
					img = PIL.Image.open(path)
					
					wpercent = (468/float(img.size[0]))
					hsize = int((float(img.size[1])*float(wpercent)))
					xlimg = img.resize((468,hsize), PIL.Image.ANTIALIAS)
					sharpener = ImageEnhance.Sharpness(xlimg)
					xlimg = sharpener.enhance(1.5)
					contraster = ImageEnhance.Contrast(xlimg)
					xlimg = contraster.enhance(1.1)
					colorizer = ImageEnhance.Color(xlimg)
					xlimg = colorizer.enhance(1.3)
					xlimgname = path + '_468.jpg'
					xlimg.save(xlimgname, 'JPEG', quality=75)
					
					wpercent = (300/float(img.size[0]))
					hsize = int((float(img.size[1])*float(wpercent)))
					limg = img.resize((300,hsize), PIL.Image.ANTIALIAS)
					sharpener = ImageEnhance.Sharpness(limg)
					limg = sharpener.enhance(1.5)
					contraster = ImageEnhance.Contrast(limg)
					limg = contraster.enhance(1.1)
					colorizer = ImageEnhance.Color(limg)
					limg = colorizer.enhance(1.3)
					limgname = path + '_300.jpg'
					limg.save(limgname, 'JPEG', quality=75)
					
					wpercent = (160/float(img.size[0]))
					hsize = int((float(img.size[1])*float(wpercent)))
					mimg = img.resize((160,hsize), PIL.Image.ANTIALIAS)
					sharpener = ImageEnhance.Sharpness(mimg)
					mimg = sharpener.enhance(1.5)
					contraster = ImageEnhance.Contrast(mimg)
					mimg = contraster.enhance(1.1)
					colorizer = ImageEnhance.Color(mimg)
					mimg = colorizer.enhance(1.3)
					mimgname = path + '_160.jpg'
					mimg.save(mimgname, 'JPEG', quality=75)
					
					os.remove(path)
					imgnames.append(iid)
				elif name != None:
					imgnames.append('notjpg')
			names.append(imgnames)
		else:
			names.append(['noattach'])
				
		concatbody = []
		for data in msg.walk():
			if data.get_content_type() == 'text/plain':
				body = data.get_payload(decode=1)
				body = str(body)
				body = string.split(body,'This message was sent using PIX-FLIX')
				body = body[0]
				concatbody.append(body)
		concatbody = "".join(concatbody)
		bodys.append(concatbody)
		subj = msg.get('subject')
		subjs.append(subj)
		
		server.dele(msgn)
			
		msgn += 1
		
	server.quit()
		
	results = zip(subjs,names,bodys)
	results = list(results)
	return results