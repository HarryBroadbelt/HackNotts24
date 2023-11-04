from nltk import word_tokenize

tokens = []
file = open('test.txt')
charstream = str(file.readlines())

tokens = word_tokenize(charstream)

for word in tokens:
