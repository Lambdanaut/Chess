# A portability module for maintaining code compatibillity between Python 2 & 3

import sys

def pyVersion():
    if sys.hexversion > 0x03000000:
        return 3
    else:
        return 2

def printMe(s):
    sys.stdout.write(str(s) + "\n")

def getInput(prompt = ""):
    if pyVersion() == 3:
        return input(prompt)
    else:
        return raw_input(prompt)