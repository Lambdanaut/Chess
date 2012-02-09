import sys, random, pymongo

import pieces
import rules
from mechanics import *

class Database:
  def __init__ (self,host,port):
    self.con = pymongo.Connection(host, port)
    self.db  = self.con.Chess
    
  def insertMove(board,x1,y1,x2,y2):
    self.db.moves.insert({
      "board": board,
      "x1"   : x1,
      "y1"   : y1,
      "x2"   : x2,
      "y2"   : y2
    }) 

class Bot:
  def __init__ (self,player):
    self.db = Database("127.0.0.1", 27017)
    self.player = player

  def doTurn(self,board):
    foundMove = self.db.db.moves.find_one({"board" : board})
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

  def learn(self,gameHistory):
    for (board,player,x1,y1,x2,y2) in gameHistory:
      if player != self.player:
        # Flip the Board
        board.reverse()
        x1=7-x1
        y1=7-y1
        x2=7-x2
        y2=7-y2
        y = 0
        for row in board:
          x = 0
          for piece in row:
            board = setPiece(board,x,y,changeOwner(piece))
            x+=1
          y += 1

        self.db.insertMove(board,x1,y1,x2,y2)
