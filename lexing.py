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
            print(word[c])
            raise Exception ("syntax error: unidentifiable characters")
    if word == "'":
        continue
    elif word[0] == "'":
        word = word.replace("'", "")
        dec = int(word, 2)
        out.append(dec)
    elif grammar.get(word) != None:
        out.append(grammar[word])
    else:
<<<<<<< HEAD
        raise Exception ("error: unrecognised command")
print(out)
parser(out)
=======
        out.append(word)
print(out)
>>>>>>> 6ff1da255e4ef0dbf894c9c7ac3bebbe3af596b0
