#Crawls and extracts data from a webpage
from urllib import urlopen 
from bs4 import BeautifulSoup
import mechanize
import re

#returns text stripped from of the HTML website
def crawl(url):
	webpage = url
	br = mechanize.Browser()
	data = br.open(webpage).get_data()

	soup = BeautifulSoup(data)

	text = (soup.get_text()).encode('utf-8').split('\n')
	#return soup
	return mineData(text)

def mineData(text):
	data = []
	for line in text:
		if '<' in line:
			nick = re.split('[<>]', line)[1]
			post = re.split('[<>]', line)[2]
			timestamp = post[-10:]
			comment = post[:-10]
			data.append(nick+"===="+comment+"-----"+timestamp)
	return data

def main():
    data =  crawl('http://logs.nodejs.org/node.js/2015-03-16')
    for x in data:
    	print(x)


if __name__ == '__main__':
    main()
exit(0)
#print soup