from commands import *

def parser(info):
    file = open("out.py", "w")
    pos = 0
    startCount = 0
    endCount = 0
    variables = []
    bracket = False
    indent = 0
    string = ''
    newline = False
    if(info[0] != 'start'):
        raise Exception ("program needs start clause")
    else:
        startCount += 1
    if(info[-1] != 'end'):
        raise Exception ("progam needs end clause")
    else:
        endCount += 1
    while(pos <= len(info)):
        pos += 1
        if( pos == len(info) - 1):
            break
        word = info[pos]
        if(word == 'start'):
            file.write(":\n")
            indent += 1
            i = indent
            while i > 0:
                i -= 1
                file.write("\t")
            startCount += 1
        elif(word == 'end'):
            file.write("\n")
            indent -= 1
            endCount += 1
        elif(word == 'else' or word == 'if' or word == 'while'):
            file.write("\n" + word + " ")
        elif(word == 'print'):
            bracket = True
            file.write("\n")
            i = indent
            while i > 0:
                i -= 1
                file.write("\t")
            file.write(word + " (")
            continue
        elif(word in grammar.values()):
            i = indent
            while i > 0:
                i -= 1
                file.write("\t")
            file.write(word + " ")
        elif(isinstance(word, int)):
            file.write(str(word) + " ")
        elif(word[0] == '1' or word[0] == '0'):
            i = indent
            while i > 0:
                i -= 1
                file.write("\t")
            i = 0
            for v in variables:
                i += 1
                if v == word:
                    num = i
            if i == 0:
                variables.append(word)
                file.write("a" + str(len(variables)) + " ")
            else:
                file.write("a" + str(i) + " ")
        else:
            file.write('"' + word + '"')
        if bracket == True:
            file.write(")\n")
            bracket = False
        

    if startCount != endCount:
        raise Exception ("cry")
    file.close()


# import math

# class Parser():
#     def __init__(self):

#         self.__parsedCommands = []
#         self.__finalParsedCommands = []

#     def readFile(self, file_name):
#         nlp = open(file_name, 'r')
#         nlp_text_found = False
#         while True:
#             char = nlp.read(1)
#             if not char:
#                 break
#             if char == "[":
#                 nlp_text_found = True
#                 continue
#             elif char == "]":
#                 nlp_text_found = False
#                 continue
#             # print(nlp_text_found)
#             if nlp_text_found == False:
#                 if char.isdigit():
#                     self.__parsedCommands.append(int(char))
#                     continue
#                 if char == "\n":
#                     self.__parsedCommands.append("\n")
#                     continue
#         nlp.close()
#         print(self.__parsedCommands)
#         reader = []
#         for i in range(len(self.__parsedCommands)):
#             print(str(self.__parsedCommands[i]))
#             if(self.__parsedCommands[i] != "\n"):
#                 print("hi")
#                 reader.append(str(self.__parsedCommands[i]))
#             else:
#                 print(reader)
#                 self.__finalParsedCommands.append("".join(reader))
#                 reader = []
#         print(self.__finalParsedCommands)
        

        

#     def getParsedCommands(self):
#         return self.__parsedCommands