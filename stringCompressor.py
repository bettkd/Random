#! /usr/bin/python
# Author: Dominic Bett
# Compress strings
# Example: aaaaabbcccccaa = a5b2c5a2

def strCompressor(string="aaabcccccaa"):
	char = [x for x in string]
	countStr = []
	count = []
	for i in range(len(char)):
		if not countStr:
			countStr.extend(char[i])
			c = 1
		else:
			if countStr[-1] == char[i]:
				c += 1
			else:
				count.append(c)
				c = 1
				countStr.extend(char[i])
			if i == (len(char)-1):
				count.append(c)
	comprStr = ""
	for j in range(len(count)):
		comprStr += countStr[j]+"%d"%count[j]
	return comprStr

def strUncompressor(string="a3b1c5a2"):
	char = [x for x in string]
	letter = []
	num = ""
	let = ""
	for char in string:
		if not letter:
			lett = char
		else:
			if char.isdigit():
				num += char
			else:
				letter.extend(lett for x in range(int(num)))
				lett = char
				num = ""
	print letter


print strCompressor()
strUncompressor()

#print countStr
#print count

