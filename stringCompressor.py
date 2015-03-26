#! /usr/bin/python
# Author: Dominic Bett
# Compress strings
# Example: aaaaabbcccccaa = a5b2c5a2
import sys
def strCompressor(string=""):
	char = [x for x in string]
	countStr = []
	strComp = ""
	for i in range(len(char)):
		if not countStr:
			countStr.extend(char[i])
			c = 1
			strComp += char[i]
		else:
			if countStr[-1] == char[i]:
				c += 1
			else:
				strComp += "%d"%c
				c = 1
				strComp += char[i]
				countStr.extend(char[i])
			if i == (len(char)-1):
				strComp += "%d"%c
	comprStr = ""
	return strComp

def strUncompressor(string=""):
	char = [x for x in string]
	letter = []
	num = ""
	let = ""
	for i in range(len(char)):
		if not letter:
			lett = char[i]
			letter.append("")
		else:
			if char[i].isdigit():
				num += char[i]
			else:
				letter.extend(lett for x in range(int(num)))
				lett = char[i]
				num = ""
			if i == (len(char)-1):
				letter.extend(lett for x in range(int(num)))
	return "".join(letter)
def main(argv):
	if len(argv)>1:
		str0 = argv[1]
	else:
		str0 = "aaaabbbbcccccccdd"
	str1 = strCompressor(string=str0)
	str2 = strUncompressor(string=str1)
	print "Initial:      %s"%str0
	print "Compressed:   %s"%str1
	print "Uncompressed: %s"%str2

if __name__ == '__main__':
	main(sys.argv)



