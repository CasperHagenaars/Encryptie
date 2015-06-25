from DualEC import *
import time
#from krommenCasper import *

curve = Elliptic_curve(4273,2,3)
P = Point(curve,26,148)
Q = Point(curve,24,73)
PRNG = Generator(P,Q,17,15)



T1 = time.time()
#curve2 = Elliptic_curve(2**256-2**224+2**192+2**96-1,-3,41058363725152142129326129780047268409114441015993725554835256314039467401291)


for i in range(0,1000):
   print([i,PRNG.INT_seed,PRNG.getNextPRN()])
   
T2 = time.time()
print(T2-T1)
    
    

