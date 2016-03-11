import sys, random, copy

import pieces
import rules
from mechanics import *

class Bot(object):
    def __init__ (self,player):
        self.player = player

    def doTurn(self, board):
        raise NotImplementedError


class RandoBot(Bot):
    """ A bot that makes random moves """
    def doTurn(self, board):
        myPieces = allPieces(board, player = self.player)
        while True:
            piece, pieceX, pieceY = random.choice(myPieces)
            possiblePiecesMoves = rules.possibleMoves(board, pieceX, pieceY)
            if possiblePiecesMoves:
                moveX, moveY = random.choice(possiblePiecesMoves)
                return (piece, pieceX, pieceY, moveX, moveY)


BOT = RandoBot