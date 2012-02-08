import sys, pymongo

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
  def __init__ (self):
    self.database = Database("127.0.0.1", 27017)

  def doTurn(self):
    pass
