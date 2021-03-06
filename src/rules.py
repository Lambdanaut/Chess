import copy

import pieces
from mechanics import *

def inCheck(board,player,mate=False):
    try: king = allPieces(board,player,pieces.ki)[0]
    except IndexError: 
        print ("FATAL ERROR: Player " + player + " doesn't have any kings, so it is not possible to get him in checkmate. ")
        exit()
    (king,kingX,kingY) = king
    if mate:
        playerPieces = allPieces(board,player)
        # Build up a list of board positions that a player could move into
        boards = []
        for (piece,x1,y1) in playerPieces:
            for (x2,y2) in possibleMoves(board,x1,y1):
                boards.append(movePiece(copy.deepcopy(board),piece,x1,y1,x2,y2) )
        boardsInCheck = []
        for b in boards:
            if not inCheck(b,player): return False 
        return True
    else:
        enemyPieces = allPieces(board,pieces.notPlayer(player) )
        for (piece,x,y) in enemyPieces:
            if isIn( (kingX,kingY), possibleMoves(board,x,y) ):
                return True
        return False

def pawnMoves(board,piece,x,y):
    possibilities = []
    player = pieceOwner(piece)

    # If the piece is on the starting lines, allow it to move two spaces. 
    if (player == pieces.w and y == 1) or (player == pieces.b and y == boardHeight(board) - 2): depth = 2
    else                                                                                      : depth = 1
    # White player rules
    if player == pieces.w:
        for i in range(y + 1, y + 1 + depth):
            if not coordInBounds(board,x,i): break
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
            if not coordInBounds(board,x,i): break
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

    if traversable(player,getPiece(board,x+1,y-2)) and coordInBounds(board,x+1,y-2): possibilities.append( (x+1,y-2) ) # 12:30
    if traversable(player,getPiece(board,x+2,y-1)) and coordInBounds(board,x+2,y-1): possibilities.append( (x+2,y-1) ) # 2:30
    if traversable(player,getPiece(board,x+2,y+1)) and coordInBounds(board,x+2,y+1): possibilities.append( (x+2,y+1) ) # 3:30
    if traversable(player,getPiece(board,x+1,y+2)) and coordInBounds(board,x+1,y+2): possibilities.append( (x+1,y+2) ) # 5:30
    if traversable(player,getPiece(board,x-1,y+2)) and coordInBounds(board,x-1,y+2): possibilities.append( (x-1,y+2) ) # 6:30
    if traversable(player,getPiece(board,x-2,y+1)) and coordInBounds(board,x-2,y+1): possibilities.append( (x-2,y+1) ) # 8:30
    if traversable(player,getPiece(board,x-2,y-1)) and coordInBounds(board,x-2,y-1): possibilities.append( (x-2,y-1) ) # 9:30
    if traversable(player,getPiece(board,x-1,y-2)) and coordInBounds(board,x-1,y-2): possibilities.append( (x-1,y-2) ) # 11:30

    return possibilities

def bishopMoves(board,piece,x,y):
    possibilities = []
    player = pieceOwner(piece)

    # Check North-East
    for (xi,yi) in zip(range(x + 1, boardWidth(board)),range(y - 1, -1, -1)):
        curPiece = getPiece(board,xi,yi)
        if not traversable(player,curPiece): break
        owner = pieceOwner(curPiece)
        possibilities.append( (xi,yi) )
        if owner != player and owner: break
    # Check South-East
    for (xi,yi) in zip(range(x + 1, boardWidth(board)),range(y + 1, boardHeight(board) ) ):
        curPiece = getPiece(board,xi,yi)
        if not traversable(player,curPiece): break
        owner = pieceOwner(curPiece)
        possibilities.append( (xi,yi) )
        if owner != player and owner: break
    # Check South-West
    for (xi,yi) in zip(range(x - 1, -1, -1),range(y + 1, boardHeight(board) ) ):
        curPiece = getPiece(board,xi,yi)
        if not traversable(player,curPiece): break
        owner = pieceOwner(curPiece)
        possibilities.append( (xi,yi) )
        if owner != player and owner: break
    # Check North-West
    for (xi,yi) in zip(range(x - 1, -1, -1),range(y - 1, -1, -1)):
        curPiece = getPiece(board,xi,yi)
        if not traversable(player,curPiece): break
        owner = pieceOwner(curPiece)
        possibilities.append( (xi,yi) )
        if owner != player and owner: break
    return possibilities

def kingMoves(board,piece,x,y):
    possibilities = []
    player = pieceOwner(piece)

    if traversable(player,getPiece(board,x,y-1)) and coordInBounds(board,x,y-1): possibilities.append( (x,y-1) )             # North
    if traversable(player,getPiece(board,x+1,y-1)) and coordInBounds(board,x+1,y-1): possibilities.append( (x+1,y-1) ) # NorthEast
    if traversable(player,getPiece(board,x+1,y)) and coordInBounds(board,x+1,y): possibilities.append( (x+1,y) )             # East
    if traversable(player,getPiece(board,x+1,y+1)) and coordInBounds(board,x+1,y+1): possibilities.append( (x+1,y+1) ) # SouthEast
    if traversable(player,getPiece(board,x,y+1)) and coordInBounds(board,x,y+1): possibilities.append( (x,y+1) )             # South
    if traversable(player,getPiece(board,x-1,y+1)) and coordInBounds(board,x-1,y+1): possibilities.append( (x-1,y+1) ) # SouthWest
    if traversable(player,getPiece(board,x-1,y)) and coordInBounds(board,x-1,y): possibilities.append( (x-1,y) )             # West
    if traversable(player,getPiece(board,x-1,y-1)) and coordInBounds(board,x-1,y-1): possibilities.append( (x-1,y-1) ) # NorthWest

    return possibilities

def queenMoves(board,piece,x,y):
    return rookMoves(board,piece,x,y) + bishopMoves(board,piece,x,y)

def possibleMoves(board,x,y):
    piece = getPiece(board,x,y)
    if   pieces.isPawn(piece):   return pawnMoves(board,piece,x,y)
    elif pieces.isRook(piece):   return rookMoves(board,piece,x,y)
    elif pieces.isKnight(piece): return knightMoves(board,piece,x,y)
    elif pieces.isBishop(piece): return bishopMoves(board,piece,x,y)
    elif pieces.isKing(piece):   return kingMoves(board,piece,x,y)
    elif pieces.isQueen(piece):  return queenMoves(board,piece,x,y)
    else:                        return []

if __name__ == '__main__':
    import boards
    board = boards.openingBoard
