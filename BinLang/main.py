from lexing import *
import subprocess

lexer('test.txt')
subprocess.run(["python", "out.py"])
