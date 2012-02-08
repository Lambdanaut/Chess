import copy

import boards
import pieces
import rules
import textDisplay as display

from mechanics import *
from portability import *

class Game:
  def __init__(self,aiOpponent,firstPlayer=pieces.w):
    self.aiOpponent = aiOpponent
    self.player = firstPlayer
    
    self.board = boards.testBoard1
    self.gameHistory = []

    self.gameLoop()

  def playerTurn(self):
    # See if the player is in Check
    if rules.inCheck(self.board,self.player):
      printMe ("You're in check! Your only valid move is to get out of check. ")
    # Read and interpret player's command
    interpretedCommand = False
    while not interpretedCommand:
      playerCommand = getInput(self.player + "'s Move: ")
      interpretedCommand = self.interpretCommand(self.board,playerCommand)
      if not interpretedCommand: printMe ("Error: Your command couldn't be read. Try again. ")
    (piece, coordX1, coordY1, coordX2, coordY2) = interpretedCommand
    # Make sure the command isn't invalid
    if pieceOwner(piece) != self.player:
      if not pieceOwner(piece): printMe ("Error: There is no piece in that position. Try again.")
      else: printMe ("Error: You don't own that piece! Try again. ")
      return self.playerTurn()
    possibleMoves = rules.possibleMoves(self.board,coordX1,coordY1)
    if not isIn((coordX2,coordY2),possibleMoves):
      printMe ("Error: That piece can not be moved there. Try again. ")
      return self.playerTurn()
    # Move the piece
    oldBoard = copy.deepcopy(self.board)
    self.board = movePiece(self.board,piece,coordX1,coordY1,coordX2,coordY2)
    # Make sure the user didn't move into check
    if rules.inCheck(self.board,self.player):
      printMe ("Error: You can't move there because you're in check. ")
      self.board = oldBoard
      return self.playerTurn()
    # Check for victory conditions
    checkmate = rules.inCheck(self.board,pieces.notPlayer(self.player),mate=True)
    if checkmate:
      printMe(display.showBoard(self.board))
      printMe("Check-mate! Player " + self.player + " wins!")
      exit()
    elif checkmate == None:
      printMe(display.showBoard(self.board))
      printMe("Stale-mate! Player " + self.player + "'s King is safe where it is, but can't move anywhere without being in check. The game is a draw! ")
      exit()

  def playerSeq(self):
    self.gameHistory.append(copy.deepcopy(self.board) )
    printMe (display.showBoard(self.board,player=self.player) )
    self.playerTurn()
    return pieces.notPlayer(self.player)

  def gameLoop(self):
    self.player = self.playerSeq()
    self.gameLoop()

  def letterToNumber(self,letter):
    return ord (letter.lower()) - 96

  def interpretCoord(self,board,coord):
    coordX = self.letterToNumber(coord[0]) - 1
    try: coordY = int(coord[1]) - 1
    except ValueError: return False
    if coordInBounds(board,coordX,coordY):
      return (coordX,coordY)
    else: return False

  def interpretCommand(self,board,command):
    splitCommand = command.split()
    if len(splitCommand) == 2:
      curLocation = splitCommand[0]
      destination = splitCommand[1]
    
      if len(curLocation) == 2 and len(destination) == 2:
        coord1 = self.interpretCoord(board, curLocation)
        coord2 = self.interpretCoord(board, destination)
        if coord1 != False and coord2 != False:
          (coordX1,coordY1) = coord1
          (coordX2,coordY2) = coord2
          piece = getPiece(board,coordX1,coordY1)
          return (piece, coordX1, coordY1, coordX2, coordY2)
        else: return False
    else: return False
