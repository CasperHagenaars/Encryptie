from krommen import *
import math

c = Elliptic_curve()
punt_public = Point(c,1,2)
q = 17
p = 29
q_maal_public = punt_public * q
p_maal_public = punt_public * p
qppublic = q_maal_public * p
pqpublic = p_maal_public * q 

print(qppublic == pqpublic)