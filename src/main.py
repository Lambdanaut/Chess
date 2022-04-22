# /usr/bin/python
#     ___  __    ____  _  _  ____  ____     ___  _   _  ____  ___  ___ 
#    / __)(  )  ( ___)( \/ )( ___)(  _ \   / __)( )_( )( ___)/ __)/ __)
#   ( (__  )(__  )__)  \  /  )__)  )   /  ( (__  ) _ (  )__) \__ \\__ \
#    \___)(____)(____)  \/  (____)(_)\_)   \___)(_) (_)(____)(___/(___/
#                         A Lambdanaut Experiment

# For python2, requires a version >= 2.6

import game

import getopt
import sys


def main():
    aiOpponents = 0

    args = sys.argv[1:]
    optlist, args = getopt.getopt(args, 'bmh')
    for (opt, arg) in optlist:

        if opt == '-h':
            print("""
            By default, running this program will start a 1v1 chess match between two human players.
            
            -b : Starts a chess game vs a minimax AI named Depthbot. 
            -m : Starts a chess game between two minimai AIs. 
            """)
            return
        elif opt == '-b':
            aiOpponents = 1
        elif opt == '-m':
            aiOpponents = 2

    game.Game(aiOpponents)


if __name__ == "__main__":
    main()
