import pieces
from mechanics import *

def pawnMoves(board,piece,x,y):
  possibilities = []
  player = pieceOwner(piece)

  # If the piece is on the starting lines, allow it to move two spaces. 
  if (player == pieces.w and y == 1) or (player == pieces.b and y == boardHeight(board) - 2): depth = 2
  else                                                                                      : depth = 1
  # White player rules
  if player == pieces.w:
    for i in range(y + 1, y + 1 + depth):
      curPiece = getPiece(board,x,i)
      if not traversable(player,curPiece): break
      owner = pieceOwner(curPiece)
      if owner == pieces.b: break
      possibilities.append( (x,i) )
    # Attack South-West
    if pieceOwner(getPiece(board, x - 1, y + 1)) == pieces.b:
      possibilities.append( (x - 1, y + 1) )
    # Attack South-East
    if pieceOwner(getPiece(board, x + 1, y + 1)) == pieces.b:
      possibilities.append( (x + 1, y + 1) )
  # Black player rules
  elif player == pieces.b:
    for i in range(y - 1, y - 1 - depth,-1):
      curPiece = getPiece(board,x,i)
      if not traversable(player,curPiece): break
      owner = pieceOwner(curPiece)
      if owner == pieces.w: break
      possibilities.append( (x,i) )
    # Attack North-West
    if pieceOwner(getPiece(board, x - 1, y - 1)) == pieces.w:
      possibilities.append( (x - 1, y - 1) )
    # Attack North-East
    if pieceOwner(getPiece(board, x + 1, y - 1)) == pieces.w:
      possibilities.append( (x + 1, y - 1) )
  return possibilities

def rookMoves(board,piece,x,y):
  possibilities = []
  player = pieceOwner(piece)

  # Check North
  for i in range(y - 1, -1, -1):
    curPiece = getPiece(board,x,i)
    if not traversable(player,curPiece): break
    owner = pieceOwner(curPiece)
    possibilities.append( (x,i) )
    if owner != player and owner: break
  # Check South
  for i in range(y + 1, boardHeight(board)):
    curPiece = getPiece(board,x,i)
    if not traversable(player,curPiece): break
    owner = pieceOwner(curPiece)
    possibilities.append( (x,i) )
    if owner != player and owner: break
  # Check East
  for i in range(x + 1, boardWidth(board)):
    curPiece = getPiece(board,i,y)
    if not traversable(player,curPiece): break
    owner = pieceOwner(curPiece)
    possibilities.append( (i,y) )
    if owner != player and owner: break
  # Check West
  for i in range(x - 1, -1, -1):
    curPiece = getPiece(board,i,y)
    if not traversable(player,curPiece): break
    owner = pieceOwner(curPiece)
    possibilities.append( (i,y) )
    if owner != player and owner: break
  return possibilities

def knightMoves(board,piece,x,y):
  possibilities = []
  player = pieceOwner(piece)

  return possibilities

def bishopMoves(board,piece,x,y):
  possibilities = []
  player = pieceOwner(piece)

  return possibilities

def kingMoves(board,piece,x,y):
  possibilities = []
  player = pieceOwner(piece)

  return possibilities

def queenMoves(board,piece,x,y):
  possibilities = []
  player = pieceOwner(piece)

  return possibilities

def possibleMoves(board,piece,x,y):
  if   pieces.isPawn(piece):   return pawnMoves(board,piece,x,y)
  elif pieces.isRook(piece):   return rookMoves(board,piece,x,y)
  elif pieces.isKnight(piece): return knightMoves(board,piece,x,y)
  elif pieces.isBishop(piece): return bishopMoves(board,piece,x,y)
  elif pieces.isKing(piece):   return kingMoves(board,piece,x,y)
  elif pieces.isQueen(piece):  return queenMoves(board,piece,x,y)
  else:                        return []
