import sys, random

import pieces
import rules
from mechanics import *

class Bot:
  def __init__ (self,player):
    self.player = player

  def doTurn(self,board):
    # If we've seen this play before, copy what we've seen. 
    if foundMove: 
      return (getPiece(board,foundMove["x1"],foundMove["y1"]),foundMove["x1"],foundMove["y1"],foundMove["x2"],foundMove["y2"])

    # If this play is new, try to play strategically. 
    else:
      myPieces = allPieces(board,player = self.player)
      while True:
        rand = random.randint(0,len(myPieces) - 1)
        (piece,x,y) = myPieces[rand]
        moves = rules.possibleMoves(board,x,y)
        if len(moves) > 0:
          (x2,y2) = moves[0]
          return (piece,x,y,x2,y2)
          break
