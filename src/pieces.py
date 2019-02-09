import portability
from mechanics import isIn

# White's ingame name
w    = "White"
# White's Pieces
pa = "pa"
ro = "ro"
kn = "kn"
bi = "bi"
ki = "ki"
qu = "qu"

# Black's ingame name
b    = "Black"
# Black's Pieces
PA = "PA"
RO = "RO"
KN = "KN"
BI = "BI"
KI = "KI"
QU = "QU"

# AI's default player
ai = b

# Empty Space on the Board
blank = "--"

# If set to True, pieces will appear as chess pieces in Unicode, but Python3 will be required.
unicodePieces = True

if portability.pyVersion() == 3 and unicodePieces:
    import unicodePieces as up
    pa = up.pa
    ro = up.ro
    kn = up.kn
    bi = up.bi
    ki = up.ki
    qu = up.qu
    PA = up.PA
    RO = up.RO
    KN = up.KN
    BI = up.BI
    KI = up.KI
    QU = up.QU
    blank = up.blank

# Sets of Pieces
wPieces   = [pa,ro,kn,bi,ki,qu]
bPieces   = [PA,RO,KN,BI,KI,QU]
allPieces = wPieces + bPieces

# Helper functions to determine piece equality
def isPawn(piece)   : return piece == pa or piece == PA
def isRook(piece)   : return piece == ro or piece == RO
def isKnight(piece) : return piece == kn or piece == KN
def isBishop(piece) : return piece == bi or piece == BI
def isKing(piece)   : return piece == ki or piece == KI
def isQueen(piece)  : return piece == qu or piece == QU

def pieceEqual(piece1,piece2):
    if   isPawn(piece1) and isPawn(piece2):     return True
    elif isRook(piece1) and isRook(piece2):     return True
    elif isKnight(piece1) and isKnight(piece2): return True
    elif isBishop(piece1) and isBishop(piece2): return True
    elif isKing(piece1) and isKing(piece2):     return True
    elif isQueen(piece1) and isQueen(piece2):   return True
    else:                                       return False

def pieceOwner(piece):
    if   isIn(piece,wPieces): return w
    elif isIn(piece,bPieces): return b
    else:                     return False

def changeOwner(piece):
    owner = pieceOwner(piece)
    if owner == w:
        if   isPawn(piece):   return PA
        elif isRook(piece):   return RO
        elif isKnight(piece): return KN
        elif isBishop(piece): return BI
        elif isKing(piece):   return KI
        elif isQueen(piece):  return QU
    elif owner == b:
        if   isPawn(piece):   return pa
        elif isRook(piece):   return ro
        elif isKnight(piece): return kn
        elif isBishop(piece): return bi
        elif isKing(piece):   return ki
        elif isQueen(piece):  return qu
    else: blank

def notPlayer(player):
    if    player == w: return b
    elif  player == b: return w
    else: return False

# The longest piece out of all of the pieces
def maxPieceLength():
    longest = 0
    for piece in allPieces:
        pieceLength = len(piece)
        if pieceLength > longest: longest = pieceLength
    return longest
maximumPieceRepresentationLength = maxPieceLength()
