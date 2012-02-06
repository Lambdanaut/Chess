import pieces

def boardWidth(board):
  return len(board[0])

def boardHeight(board):
  return len(board)

def coordInBounds (board,x,y):
  if x >= 0 and x < boardWidth(board) and y >= 0 and y < boardHeight(board): return True
  else: return False

def isIn(el,l):
  for element in l:
    if el == element:
      return True
  return False

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
  if not piece: return False
  if piece == pieces.blank: return False
  if isIn(piece, pieces.wPieces):
    return pieces.w
  else: return pieces.b

def traversable(player,piece):
  if pieceOwner(piece) != player or piece == pieces.blank: return True
  else: return False

# Returns a [(piece,x,y)]
def allPieces(board,player = None,pieceType = None):
  playerPieces = []
  y = 0
  dynamicPieceType = pieceType
  for row in board:
    x = 0
    for piece in row:
      if not pieceType:
        dynamicPieceType = piece
      if player:
        if pieceOwner(piece) == player and pieces.pieceEqual(piece,dynamicPieceType) : playerPieces.append( (piece,x,y) )
      else:
        if piece != pieces.blank and pieces.pieceEqual(piece,dynamicPieceType): playerPieces.append( (piece,x,y) )
      x += 1
    y += 1
  return playerPieces
