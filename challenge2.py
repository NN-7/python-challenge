'''
URL: http://www.pythonchallenge.com/pc/def/ocr.html

Image of a book, with a text below saying:
'recognize the characters. maybe they are in the book, but MAYBE they are in the page source.'

Solution:

Open page source (inspect) Right Click, inspect OR CTRL+SHIFT+I

Scroll down, you'll see text saying "find rare characters in the mess below"

Count all the letters in the text and you'll find the rare letters: e,q,u,a,l,i,t,y

So we change http://www.pythonchallenge.com/pc/def/ocr.html
to http://www.pythonchallenge.com/pc/def/equality.html
'''

text = open('challenge2.txt', 'r').read()

def challenge2(text):
	count = {}
	seen = ""
	for letter in text:
		if letter not in seen:
			seen += letter
			count.update({letter: 1})
		else:
			count[letter] += 1
	return count

print(challenge2(text))