import math
#import Bisection

class Point:
    def __init__(self,curve,x,y,inf = False):
        self.x = x
        self.y = y
        self.curve = curve
        self.inf = inf #TODO: this will bug if we declare 0,0 as point
        if not self.onCurve():
            print("Punt ("+str(x)+","+str(y)+") niet op kromme")
            
    def __str__(self):
        return str("(x,y) = ("+str(self.x)+","+str(self.y)+")")
            
    def __eq__(self,other):
        if other == None:
            return False
        if other.inf == True and self.inf == True:
            return True
        elif other.inf == True or self.inf == True:
            return False
        else:
            marge = 0.00001
            return (math.fabs(self.x - other.x) < marge and math.fabs(self.y - other.y) < marge)
        

        
    def _findninv(self,n):
        if n == 1:
            return 1
        if n == 0:
            #print('Inverse of 0 asked for, returning 0')
            return 0
        p = self.curve.p
        ninv = n**(p - 2) # gebruik Euler totient functie
        ninv = ninv % p
        return ninv
           
        
    def _double(self): # Dubbellen van punten op EC over Fp, p priem
        #print('Working double called')
        if self.inf == True: # Dubbel van 0 is 0
            print('Error, something in __add__ is allowing through cases that should be filtered')
            return self
        x = self.x
        y = self.y
        if y == 0:
            return Point(self.curve,0,0,True)
        a = self.curve.a
        p = self.curve.p
        if not (type(x) == long or type(x) == int):
            print('Error detected. Trying to double point with non integer x')
            print(type(x))
        if not (type(y) == long or type(y) == int):
            print('Error detected. Trying to double point with non integer y')
        #bereken s geheeltallig:
        t = 3*x*x + a # teller
        n = 2*y # noemer
        ninv = self._findninv(n) # om s geheel te houden willen we niet met breuk werken, dus doen we s = ninv * t
        s = (t * ninv) % p
        xr = (s*s - 2*x) % p
        yr = (-y + s*(x - xr)) % p
        rtpoint = Point(self.curve,xr,yr)
        return rtpoint
        
#        2P = R where 

#s = (3xP2 + a) / (2yP ) mod p 

#xR = s2 - 2xP mod p and yR = -yP + s(xP - xR) mod p
        
    def __add__(self,other): # definieert additie van geheelwaardige punten op krommen over Fp, p priem
        #print('Adding '+str(self)+' to '+str(other))
        if self == other:
            return self._double()
        if self.inf == True:
            return other
        if other.inf == True:
            return self
        if other == Point(self.curve,0,0,True):
            print('Zero addition')
            return self
        if self == Point(self.curve,0,0,True):
            print('Zero addition')
            return other
        else:
            p = self.curve.p
            xp = self.x
            xq = other.x
            yp = self.y
            yq = other.y
            t = yq - yp
            n = xq - xp
            if n == 0: # zelfde x waarde betekent inverse
                print(str(self),str(other))
                return Point(self.curve,0,0,True)
            ninv = self._findninv(n)
            s = (t*ninv) % p # zorgt voor geheeltallige s
            xr = (s*s - xp - xq) % p
            yr = (s*(xp - xr) - yp) % p
            return Point(self.curve,xr, yr)
            
    def mul(self,n):
        if not (isinstance(n,int)):
            print('Wrong type of multiplication')
            return None
        punt = self
        for _ in range(n-1):
            punt += self
            #print(punt
        return punt    
        
    def mulsnel(self,INT_n):
        if not (isinstance(INT_n,int)):
            print('Wrong type of multiplication')
            return None
        STR_binary = bin(INT_n)[2:] #maak van het getal binaire code
        INT_mostsigbit = len(STR_binary)
        POINT_answer = None
        POINT_currentdouble = self
        for bitnr in range(INT_mostsigbit-1,-1,-1): #go through starting at least significant bit
            CHAR_bit = STR_binary[bitnr]
            if CHAR_bit == '1':
                #print('1 gevonden')
                if POINT_answer == None:
                   #print('Eerste 1 gevonden')
                    POINT_answer = POINT_currentdouble
                else :
                    POINT_answer += POINT_currentdouble
            POINT_currentdouble = POINT_currentdouble + POINT_currentdouble
        return POINT_answer
                
        
    def __mul__(self,n):
        if self.inf == True:
            return self
        return self.mulsnel(n)

    def __neg__(self):
        if self.inf == True:
            return self
        ry= -self.y % self.curve.p
        return Point(self.curve, self.x, ry) 
        

    def __sub__(self,other):
        print('Sub called')
        return self + (-other)
    
    def onCurve(self):
        if self.inf == True:
            return True
        marge = 0.0001
        x = self.x
        y = self.y
        p = self.curve.p
        a = self.curve.a
        b = self.curve.b
        lhs = y**2 % p
        rhs = (x**3 + x*a + b) % p
        if lhs == rhs:
            return True
        else:
            print(str(lhs)+' != '+str(rhs))
            return False
        return (y**2 % p - (x**3 + x*a + b) % p) < marge
        return  math.fabs(self.x**3 + self.curve.a*self.x + self.curve.b - self.y*self.y) < marge
            
class Elliptic_curve:
    def __init__(self,p=17,a=2,b=2):
        self.a = a
        self.b = b
        self.p = p
        if (4*self.a**3+27*self.b**2) % self.p == 0:
            print("Deze curve definieert geen groep onder modulo "+str(self.p))
        
    def __str__(self):
        string = "Vergelijking: y^2 = x^3 + " + str(self.a) + "x + " + str(self.b)
        return string
        
    def findStartingPoint(self):
        return
        #priemfactorisatie
        #O(subgroep) | orde(groep)
        #Als niet kleinste subgroep, dan is het grote subgroep
        
    def giveY(self,x):
        #returns positive y
        return math.sqrt(x**3 + self.a*x + self.b)
    
    def points(self):
        punten = ["inf"]
        p = self.p
        for x in range(p):
            for y in range(p):
                if (y**2) % p == (x**3+self.a*x + self.b) % p:
                   punten.append((x,y)) 
        return punten
                
    def __eq__(self,other):
        marge = 0.000001
        return abs(self.a-other.a) < marge and abs(self.b-other.b) < marge
        #return self.a == other.a and self.b == other.b

#curve = Elliptic_curve()
#punt_p = Point(curve,1,2)
#punt_q = Point(curve,-7/4,-27/8)