from generator import *
from krommen import * 
from DH import *
from Backdoor import *

print("We kiezen a, b, p en de seed.")
# y^2 (mod p) = x^3 + a*x + b (mod p)
a = 2
print("a = " + str(a))
b = 16
print("b = " + str(b))
p = 4093082899
print("p = " + str(p))
seed = 123596
print("seed = " + str(seed))
curve = EllipticCurve(p,a,b) # curve gedefinieerd
print("Dan kiezen we een punt P en bepalen we Q aan de hand van P*e, wat voor de backdoor zorgt")
P = Point(curve,0,4)
e = 45653
Q = P*e 
print("Orde van F(p) = " + str(P.findOrder()))
d = P.createBackdoor(e) # berekenen van d zodat P = Q*e
print("Dan berekenen we d zodat P = Q*e")
print()
print("P = " + str(P))
print("Q*d = " + str(Q) + "*" + str(d) + " = " + str(Q*d))
print("Q = " + str(Q))
print("P*e = " + str(P) + "*" + str(e) + " = " + str(P*e))
print()
print("Klein voorbeeld van de Diffie-Hell sleuteluitwisselingsprotocol:")
Diffie = DH(P,123,456,curve)
print()
print("En nu de PRNG:")
PRNG = Generator(P,Q,seed)

output1 = PRNG.generate()               # de eerste twee worden opgeslagen om de seed te berekenen
output2 = PRNG.generate()               
for n in range(10):
    print(PRNG.generate())
    
print()
print("En nu met behulp van de eerste twee outputs en de backdoor kan de volgende seed en daarmee de rest van de output voorspeld worden")
print("Hier wordt dezelfde reeks, ongetrunceerd, geprint, door gebruik te maken van de eerste twee output en de backdoor:")
print()
BD = Backdoor(PRNG,[output1,output2],d) # initiëren van de backdoor
seed = BD.findSeed()                    # vind de seed
for _ in range(10):
    seed = (P*seed).x                   # bereken de volgende seed
    print((Q*seed).x)                   # print de output, maar dan ongetrunceerd