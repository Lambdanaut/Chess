#CHESS

import boards
import pieces

from portability import *

debug = True

def possibleMoves(board,piece,x,y):
  possibilities = []
  player = pieceOwner(piece)
  # Rook
  if pieces.isRook(piece):
    # Check North
    deep=False
    for i in range(y - 1, -1, -1):
      if deep: break
      curPiece = getPiece(board,x,i)
      if traversable(player,curPiece): 
        owner = pieceOwner(curPiece)
        if owner != player and owner: deep = True
        possibilities.append( (x,i) )
      else: break
    # Check South
    deep=False
    for i in range(y + 1, boardHeight(board)):
      if deep: break
      curPiece = getPiece(board,x,i)
      if traversable(player,curPiece):
        owner = pieceOwner(curPiece)
        if owner != player and owner: deep = True
        possibilities.append( (x,i) )
      else: break
    # Check East
    deep=False
    for i in range(x + 1, boardWidth(board)):
      if deep: break
      curPiece = getPiece(board,i,y)
      if traversable(player,curPiece):
        owner = pieceOwner(curPiece)
        if owner != player and owner: deep = True
        possibilities.append( (i,y) )
      else: break
    # Check West
    deep=False
    for i in range(x - 1, -1, -1):
      if deep: break
      curPiece = getPiece(board,i,y)
      if traversable(player,curPiece):
        owner = pieceOwner(curPiece)
        if owner != player and owner: deep = True
        possibilities.append( (i,y) )
      else: break

  return possibilities

def letterToNumber(letter):
  return ord (letter.lower()) - 96

def isIn(el,l):
  for element in l:
    if el == element:
      return True
  return False

def boardWidth(board):
  return len(board[0])

def boardHeight(board):
  return len(board)

def coordInBounds (board,x,y):
  if x >= 0 and x < boardWidth(board) and y >= 0 and y < boardHeight(board): return True
  else: return False

def getPiece(board,x,y):
  if coordInBounds(board,x,y): return board[y][x]
  else: return False

def setPiece(board,x,y,piece):
  if coordInBounds(board,x,y):
    newBoard = board
    newBoard[y][x] = piece
    return newBoard
  else: return False

def movePiece(board,piece,coordX1,coordY1,coordX2,coordY2):
  b1 = setPiece(board,coordX1,coordY1,pieces.blank)
  b2 = setPiece(b1,   coordX2,coordY2,piece)
  return b2

def pieceOwner(piece):
  if piece == pieces.blank: return False
  if isIn(piece, pieces.wPieces):
    return 'w'
  else: return 'b'

def traversable(player,piece):
  if pieceOwner(piece) != player or piece == pieces.blank: return True
  else: return False

def interpretCoord(board,coord):
  coordX = letterToNumber(coord[0]) - 1
  try: coordY = int(coord[1]) - 1
  except ValueError: return False
  if coordInBounds(board,coordX,coordY):
    return (coordX,coordY)
  else: return False

def interpretCommand(board,command):
  splitCommand = command.split(" ")
  if len(splitCommand) == 2:
    curLocation = splitCommand[0]
    destination = splitCommand[1]
    
    if len(curLocation) == 2 and len(destination) == 2:
      coord1 = interpretCoord(board, curLocation)
      coord2 = interpretCoord(board, destination)
      if coord1 != False and coord2 != False:
        (coordX1,coordY1) = coord1
        (coordX2,coordY2) = coord2
        piece = getPiece(board,coordX1,coordY1)
        return (piece, coordX1, coordY1, coordX2, coordY2)
      else: return False
  else: return False

def showPiece(piece):
  pieceRep = piece
  while len(pieceRep) < pieces.maximumPieceRepresentationLength:
    pieceRep += " "
  return pieceRep

def showBoard(board,withCoords=True):
  boardRep = ""
  if withCoords:
    rowCoord = 1
    boardRep += "    "
    for coord in ['a','b','c','d','e','f','g','h']:
      boardRep += showPiece(coord) + " "
    boardRep += "\n\n"
  for row in board:
    if withCoords:
      boardRep += str(rowCoord) + "   "
      rowCoord += 1
    for piece in row:
      boardRep += showPiece(piece) + " "
    boardRep += "\n"
  return boardRep

def playerTurn(board,player):
  print ("It is \"" + player + "\"'s turn. ")
  interpretedCommand = False
  while not interpretedCommand:
    playerCommand = getInput()
    interpretedCommand = interpretCommand(board,playerCommand)
    if not interpretedCommand: print ("Error: Your command couldn't be read. Try again. ")
  (piece, coordX1, coordY1, coordX2, coordY2) = interpretedCommand
  if pieceOwner(piece) != player:
    if not pieceOwner(piece): print ("Error: There is no piece in that position. Try again.")
    else: print ("Error: You don't own that piece! Try again. ")
    return playerTurn(board,player)
  piecesPossibleMoves = possibleMoves(board,piece,coordX1,coordY1)
  if not isIn((coordX2,coordY2),piecesPossibleMoves):
    print ("Error: That piece can not be moved there. Try again. ")
    return playerTurn(board,player)
  movePiece(board,piece,coordX1,coordY1,coordX2,coordY2)
  return board

def gameLoop(board):
  print (showBoard(board))
  boardAfterWhite = playerTurn(board,"w")
  print (showBoard(boardAfterWhite))
  boardAfterBlack = playerTurn(boardAfterWhite,"b")
  gameLoop(boardAfterBlack)

def startGame(board):
  gameLoop(board)
  
def main():
  startGame(boards.testBoard1)  

if __name__ == "__main__": main()
