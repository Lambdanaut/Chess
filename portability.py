# A portability module for maintaining code compatibillity between Python 2 & 3

import sys

def pyVersion():
  if sys.hexversion > 0x03000000:
    return 3
  else:
    return 2

def getInput():
  if sys.hexversion > 0x03000000:
    return input()
  else:
    return raw_input()
