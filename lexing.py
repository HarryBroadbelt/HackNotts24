from nltk import word_tokenize
from commands import *
from parserrr import *

tokens = []
file = open('test.txt')
charstream = str(file.readlines())

tokens = word_tokenize(charstream)
words = [word for word in tokens if word not in ['[', ']', "''", '``']]
out = []

for word in words:
    for c in range(0, len(word)):
        if (word[c]) not in ["1", "0", "'"]:
            raise Exception ("syntax error: unidentifiable character: " + c)
    if word == "'":
        continue
    elif word[0] == "'":
        word = word.replace("'", "")
        dec = int(word, 2)
        out.append(dec)
    elif grammar.get(word) != None:
        out.append(grammar[word])
    else:
        out.append(word)
print(out)
