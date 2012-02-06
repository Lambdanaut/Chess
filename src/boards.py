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
[RO,KN,BI,QU,KI,BI,KN,RO]
]

blankBoard = [ [xx for x in range(0,8)] for y in range(0,8) ]

testBoard1 = [
[ro,xx,xx,xx,xx,xx,xx,ro],
[xx,pa,pa,pa,pa,pa,pa,pa],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[xx,xx,xx,xx,xx,xx,xx,xx],
[PA,PA,PA,PA,PA,PA,PA,xx],
[RO,KN,BI,KI,QU,BI,KN,RO]
]
