import urllib2
from urllib2 import urlopen
import cookielib
from cookielib import CookieJar
import re
import time

cj = CookieJar() # Not absolutely necessary but recommended
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')] # To be able to crawl on websites that blocks Robots

def readSourceCode():
	try:
		page = 'http://logs.nodejs.org/node.js/index'
		sourceCode = opener.open(page).read()
		return sourceCode
	except Exception, e:
		print str(e)

def scrapLinks(sourceCode):
	try:
		links = re.findall(r'<a href="(.*?)">',sourceCode)
		return links
	except Exception, e:
		print str(e)

def main():
	for x in scrapLinks(readSourceCode()):
		print x

if __name__ == '__main__':
	main()