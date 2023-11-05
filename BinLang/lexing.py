from nltk import word_tokenize
from commands import *
from parserrr import *

def lexer(testfile):
    tokens = []
    file = open(testfile)
    charstream = str(file.readlines())

    tokens = word_tokenize(charstream)
    words = [word for word in tokens if word not in ['[', ']', "''", '``']]
    out = []
    if words[-1] == "'":
        words.pop()

    strin = False
    wordsss = ""
    print(words)
    for word in words:
        for c in range(0, len(word)):
            if (word[c]) not in ["1", "0", "'" ,"-"]:
                raise Exception ("syntax error: unidentifiable character: " + c)
        if word == "'" and out != []:
            out.append(wordsss)
            wordsss = ""
            strin = False
            continue
        elif word == "'" or word == "":
            continue
        elif word[0] == "-" and word[-1] == "-":
            word = word.strip('-')
            dec = int(word, 2)
            out.append(dec)
        elif word[0] == "'" and word != "'":
            strin = True
            word = word.replace("'", "")
            dec = int(word, 2)
            new = chr(dec)
            wordsss += new
            continue
        elif strin == True:
            dec = int(word, 2)
            new = chr(dec)
            wordsss += new
        elif grammar.get(word) != None:
            out.append(grammar[word])
        else:
            out.append(word)
    print(out)
    parser(out)
