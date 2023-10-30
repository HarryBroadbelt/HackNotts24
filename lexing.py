from nltk import word_tokenize
from commands import *
from parserrr import *
import binascii

tokens = []
file = open('test2.txt')
charstream = str(file.readlines())

tokens = word_tokenize(charstream)
words = [word for word in tokens if word not in ['[', ']', "''", '``']]
out = []

print(words)
for word in words:
    for c in range(0, len(word)):
        if (word[c]) not in ["1", "0", "'" ,"-"]:
            raise Exception ("syntax error: unidentifiable character: " + c)
    if word == "'":
        continue
    if word[0] == "-" and word[-1] == "-":
        word = word.strip('-')
        dec = int(word, 2)
        out.append(dec)
    elif word[0] == "'":
        word = word.replace("'", "")
        new = binascii.b2a_uu(word.encode())
        out.append(new)
    elif grammar.get(word) != None:
        out.append(grammar[word])
    else:
        out.append(word)
print(out)
parser(out)
