from commands import *

def parser(info):
    file = open("out.txt", "w")
    pos = 0
    startCount = 0
    endCount = 0
    varnum = 0
    if(info[pos] != '1'):
        raise Exception ("program needs start clause")
    else:
        startCount += 1
    if(info[-1] != '0'):
        raise Exception ("progam needs end clause")
    else:
        endCount += 1
    while(info != []):
        pos += 1
        if(info[pos] == 'start' and info[pos - 2] == "if"):
            startCount += 1
        elif(info[pos] == 'end'):
            endCount += 1
        elif(grammar.get(info[pos]) != None):

        

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