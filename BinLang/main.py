from lexing import *
import subprocess

lexer('hello_world.txt')
subprocess.run(["python", "out.py"])
