# /usr/bin/python
#     ___  __    ____  _  _  ____  ____     ___  _   _  ____  ___  ___ 
#    / __)(  )  ( ___)( \/ )( ___)(  _ \   / __)( )_( )( ___)/ __)/ __)
#   ( (__  )(__  )__)  \  /  )__)  )   /  ( (__  ) _ (  )__) \__ \\__ \
#    \___)(____)(____)  \/  (____)(_)\_)   \___)(_) (_)(____)(___/(___/
#                         A Lambdanaut Experiment

# For python2, requires a version >= 2.6

import game
import getopt, sys

def main():
    aiOpponents = 0

    args = sys.argv[1:]
    optlist, args = getopt.getopt(args, 'bm')
    for (opt, arg) in optlist:
        if opt == '-b': aiOpponents = 1
        if opt == '-m': aiOpponents = 2

    game.Game(aiOpponents)

if __name__ == "__main__": main()