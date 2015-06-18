from PCclass import *
from krommen import *

E = Elliptic_curve()
print(E)
point = Point(E,1,2)
mycomp = PC('Alice',E,point,3)
othercomp = PC('Bob',E,point,4)
print(mycomp)
print(othercomp)
mycomp.messageToCode('Hello World',othercomp)
