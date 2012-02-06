import portability

# White's ingame name
w  = "White"
# White's Pieces
pa = "pa"
ro = "ro"
kn = "kn"
bi = "bi"
ki = "ki"
qu = "qu"

# Black's ingame name
b  = "Black"
# Black's Pieces
PA = "PA"
RO = "RO"
KN = "KN"
BI = "BI"
KI = "KI"
QU = "QU"

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
  KN = up.KI
  BI = up.BI
  KI = up.KI
  QU = up.QU
  blank = up.blank

# Sets of Pieces
wPieces   = [pa,ro,kn,bi,ki,qu]
bPieces   = [PA,RO,KN,BI,KI,QU]
allPieces = wPieces + bPieces

# Helper functions to determine piece equality
def isPawn(piece)  : return piece == pa or piece == PA
def isRook(piece)  : return piece == ro or piece == RO
def isKnight(piece): return piece == kn or piece == KN
def isBishop(piece): return piece == bi or piece == BI
def isKing(piece)  : return piece == ki or piece == KI
def isQueen(piece) : return piece == qu or piece == QU

# The longest piece out of all of the pieces
def maxPieceLength():
  longest = 0
  for piece in allPieces:
    pieceLength = len(piece)
    if pieceLength > longest: longest = pieceLength
  return longest
maximumPieceRepresentationLength = maxPieceLength()

