import boards
import pieces
import rules
import textDisplay as display

from mechanics import *
from portability import *

def letterToNumber(letter):
  return ord (letter.lower()) - 96

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

def playerTurn(board,player):
  # See if the player is in Check
  if rules.inCheck(board,player):
    printMe ("You're in check! Your only valid move is to get out of check. ")
    inCheck = True
  else: inCheck = False
  # Read and interpret player's command
  interpretedCommand = False
  while not interpretedCommand:
    playerCommand = getInput(player + "'s Move: ")
    interpretedCommand = interpretCommand(board,playerCommand)
    if not interpretedCommand: printMe ("Error: Your command couldn't be read. Try again. ")
  (piece, coordX1, coordY1, coordX2, coordY2) = interpretedCommand
  # Make sure the command isn't invalid
  if pieceOwner(piece) != player:
    if not pieceOwner(piece): printMe ("Error: There is no piece in that position. Try again.")
    else: printMe ("Error: You don't own that piece! Try again. ")
    return playerTurn(board,player)
  possibleMoves = rules.possibleMoves(board,piece,coordX1,coordY1)
  if not isIn((coordX2,coordY2),possibleMoves):
    printMe ("Error: That piece can not be moved there. Try again. ")
    return playerTurn(board,player)
  # Move the piece
  newBoard = movePiece(board,piece,coordX1,coordY1,coordX2,coordY2)
  # Check for victory conditions
  if rules.inCheck(board,pieces.notPlayer(player),mate=True):
    printMe(display.showBoard(newBoard))
    printMe("Check-mate! Player " + player + " wins!")
    exit()
  print board,newBoard
  return newBoard

def gameLoop(board):
  printMe (display.showBoard(board,player=pieces.w))
  boardAfterWhite = playerTurn(board,pieces.w)
  printMe (display.showBoard(boardAfterWhite,player=pieces.b))
  boardAfterBlack = playerTurn(boardAfterWhite,pieces.b)
  gameLoop(boardAfterBlack)

def startGame():
  gameLoop(boards.openingBoard)
