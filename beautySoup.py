from urllib import urlopen 
from bs4 import BeautifulSoup
import mechanize
import re

webpage = 'http://logs.nodejs.org/node.js/2015-03-16'
br = mechanize.Browser()
data = br.open(webpage).get_data()

soup = BeautifulSoup(data)

text = (soup.get_text()).encode('utf-8').split('\n')
for line in text:
	if '<' in line:
		nick = re.split('[<>]', line)[1]
		post = re.split('[<>]', line)[2]
		timestamp = post[-9:]
		comment = post[:-9]
		print nick, "====", comment, "-----", timestamp

#print soup