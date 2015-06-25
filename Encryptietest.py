from krommenCasper import *
import math
import time
import sys
T1 = time.time()
c = Elliptic_curve(4273,2,3)
P = Point(c,26,148)
Q = Point(c,1134,660)
R = Point(c,3531,14)
S = Point(c,1172,2824)
q = 101
p = 101
print(c)
getal = Point(c,0,0,True)
print(P*2+P*2)
print(R+R)
print(P + Q)
for i in range(1,3000):
    getal += P
    if getal.inf == True:
        break
    print(i,str(getal))
print('-----------------------------------------------------------------------------------------------------------')
print(len(c.points()))
T2 = time.time()
print(T2-T1)