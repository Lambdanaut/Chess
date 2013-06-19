import sys, random, copy

import pieces
import rules
from mechanics import *

class Bot:
  def __init__ (self,player):
    self.player = player
    self.learning_iterations = 10

  def doTurn(self,board):
    for iteration in range(0,self.learning_iterations)
      curBoard = board
      curPlayer = 
      myPieces = allPieces(curBoard,player = self.player)
      random.shuffle(myPieces)
      openingMove = None
      for piece in myPieces:
        (p,x,y) = piece
        possibleMoves = rules.possibleMoves(board,x,y)
        if possibleMoves:
          randomMoveIndex = random.randint(0,len(possibleMoves) - 1)
          randomMove = possibleMoves[randomMoveIndex]
          break
      sys.exit("Error: AI has no possible moves. ")


        return (getPiece(board,foundMove["x1"],foundMove["y1"]),foundMove["x1"],foundMove["y1"],foundMove["x2"],foundMove["y2"])

        while True:
          rand = random.randint(0,len(myPieces) - 1)
          (piece,x,y) = myPieces[rand]
          moves = rules.possibleMoves(board,x,y)
          if len(moves) > 0:
            (x2,y2) = moves[0]
            return (piece,x,y,x2,y2)
            break