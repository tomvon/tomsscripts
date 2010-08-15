"""This script will remove "nasty" characters from a string. 
Useful for sanitizing file ids."""

def clean(anyid):
	
	import string

	anyid = str(anyid)
	
	anyid = string.replace(anyid,' ','_')
	anyid = string.replace(anyid,'-','_')
	anyid = string.replace(anyid,'"','')
	anyid = string.replace(anyid,'\'','')
	anyid = string.replace(anyid,'&','and')
	anyid = string.replace(anyid,'\,','')
	anyid = string.replace(anyid,'!','')
	anyid = string.replace(anyid,'@','')
	anyid = string.replace(anyid,'#','')
	anyid = string.replace(anyid,'$','')
	anyid = string.replace(anyid,'%','')
	anyid = string.replace(anyid,'^','')
	anyid = string.replace(anyid,'*','')
	anyid = string.replace(anyid,'\(','')
	anyid = string.replace(anyid,'\)','')
	anyid = string.replace(anyid,';','')
	anyid = string.replace(anyid,'|','')
	anyid = string.replace(anyid,'+','')
	anyid = string.replace(anyid,'~','')
	anyid = string.replace(anyid,'\[','')
	anyid = string.replace(anyid,'\]','')
	anyid = string.replace(anyid,'\{','')
	anyid = string.replace(anyid,'\}','')
	anyid = string.replace(anyid,'?','')
	
	return anyid