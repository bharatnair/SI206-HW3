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

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

a_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
a_surs = urllib.request.urlopen(a_url).read()
soup = BeautifulSoup(a_surs, 'html.parser')

# print (type(a_surs))
# print (type(soup))

# for x in soup.find_all("p"):
# 	if "student" in x.text:
# 		print (x)

for x in soup.

print ("\nlol\n")
# f_create_local_html = open("localhyper.html", "w")
# f_create_local_html.write(str(text11111))
# f_create_local_html.close()