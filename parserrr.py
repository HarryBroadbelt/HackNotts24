from commands import *

def parser(info):
    file = open("out.py", "w")
    pos = 0
    startCount = 0
    endCount = 0
    variables = []
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
        word = info[pos]
        if(word == 'start' and info[pos - 2] == "if"):
            file.write("if")
            startCount += 1
        elif(word == 'end'):
            endCount += 1
        elif(word in grammar.values()):
            file.write(word)
        elif(isinstance(word, int)):
            file.write(str(word))
        else:
            variables.append(word)
            file.write("a" + str(len(variables)))

        

    if startCount != endCount:
        raise Exception ("cry")




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