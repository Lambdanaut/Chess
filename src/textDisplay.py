import pieces

def showPiece(piece):
  pieceRep = piece
  while len(pieceRep) < pieces.maximumPieceRepresentationLength:
    pieceRep += " "
  return pieceRep

def showBoard(board,withCoords=True,player=None):
  boardRep = ""
  if player:
    boardRep += ("" + player + "'s Turn\n")
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

