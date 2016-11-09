# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

print ()
print ("*** SI 206 - HW 3 - BeautifulSoup Program ***")
print ("\nName: Bharat Nair\nUniqname: bnair")

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

a_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
a_surs = urllib.request.urlopen(a_url).read()
soup = BeautifulSoup(a_surs, 'html.parser')

#the code below replaces all instances of "student" with "AMAZING student"
for x in soup.find_all(string=re.compile("student")):
	x.string.replace_with(x.string.replace("student", "AMAZING student"))
	#x.replace_with(x.replace("student", "AMAZING student")) #does the same thing

#the code below add my own local sources for the images in the newly created html
for y in soup.find_all("img"):
	if y['src'] == "logo2.png":
		y['src'] = "media/logo.png"
	else:
		y['src'] = "media/bn_pic.jpeg"

#this code creates and writes the local html files
try:
	f_create_local_html = open("localhyper.html", "w")
	f_create_local_html.write(str(soup))
	f_create_local_html.close()
	print ("\nLocal HTML called 'localhyper.html' has been successfully created!\n")
except:
	print ("\nOh no, an error occured when trying to create 'localhyper.html'. Oops!\n")








