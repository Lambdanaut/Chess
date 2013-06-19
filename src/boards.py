from pieces import blank as xx
from pieces import *

openingBoard = [
[ro,kn,bi,ki,qu,bi,kn,ro],
[pa,pa,pa,pa,pa,pa,pa,pa],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[PA,PA,PA,PA,PA,PA,PA,PA],
[RO,KN,BI,KI,QU,BI,KN,RO]
]

blankBoard = [ [xx for x in range(0,8)] for y in range(0,8) ]

testBoard1 = [
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,ki,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,pa,xx,xx,xx],
[xx,xx,xx,xx,KI,xx,xx,xx]
]
testBoard2 = [
[ro,kn,xx,ki,qu,bi,kn,ro],
[pa,pa,pa,xx,pa,pa,pa,pa],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,KN,PA,xx,bi,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[PA,PA,PA,PA,xx,xx,xx,PA],
[RO,KN,BI,KI,BI,PA,xx,RO]
]