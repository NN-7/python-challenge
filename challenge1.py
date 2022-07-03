"""
URL: http://www.pythonchallenge.com/pc/def/map.html

A notebook with text written on it that says:
K -> M
O -> Q
E -> G

Below, there are two bodies of text:

'everybody thinks twice before solving this.',
and
'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

Solution:

Each map is to a letter that is two letters ahead. (k,l,m),(e,f,g),(o,p,q)

So a -> c, b -> d, etc.

Function solution can be found.

Applied on URL:

map -> ocr
"""

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def challenge1(text):
	abc = "abcdefghijklmnopqrstuvwxyz"
	ignore = " .()'"
	ntext = ""
	for letter in text:
		if letter in ignore:
			ntext += letter
			continue
		spot = abc.index(letter)
		if spot >= 24:
			spot -= 24
		else:
			spot += 2
		letter = abc[spot]
		ntext += letter
	return ntext

print(challenge1(text))