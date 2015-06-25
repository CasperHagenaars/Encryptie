import math
#import Bisection

class Point:
    def __init__(self,curve,x,y,inf=False):
        self.marge = curve.marge #marge eenmaal gedefinieerd in curve
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
            marge = self.marge
            return (math.fabs(self.x - other.x) < marge and math.fabs(self.y - other.y) < marge)
        
    def _findninv(self,n):
        if n == 1 or n == 0:
            return n
        p = self.curve.p
        ninv = n**(p - 2) # gebruik Euler totient functie
        ninv = ninv % p
        return ninv
           
    def __add__(self,other): # definieert additie van geheelwaardige punten op krommen over Fp, p priem
        #print('Adding '+str(self)+' to '+str(other))
        if self.inf == True:
            return other
        if other.inf == True:
            return self
        if self == other:
            x = self.x
            y = self.y
            if y == 0:
                return Point(self.curve,0,0,True)
            a = self.curve.a
            p = self.curve.p
            if not (type(x) == int and type(y) == int): # de long type bestaat niet meer in python3*
                print('Error detected. Trying to double point with non integer x')
                print("type(x) = "+ str(type(x))+ ", type(y): " + str(type(y)))
            t = 3*x**2 + a # teller
            n = 2*y # noemer
            ninv = self._findninv(n) # om s geheel te houden willen we niet met breuk werken, dus doen we s = ninv * t
            s = (t * ninv) % p
            xr = (s*s - 2*x) % p
            yr = (-y + s*(x - xr)) % p
            rtpoint = Point(self.curve,xr,yr)
            return rtpoint
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
            
    def __mul__(self,INT_n):
        if self.inf == True:
            return self
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

    def __neg__(self):
        if self.inf == True:
            return self
        ry = -self.y % self.curve.p
        return Point(self.curve, self.x, ry) 
        
    def __sub__(self,other):
        return self + (-other)
    
    def onCurve(self):
        if self.inf == True:
            return True
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
            print(str(lhs) + ' != ' + str(rhs))
            return False
            
class Elliptic_curve:
    def __init__(self,p=17,a=2,b=2):
        self.a = a
        self.b = b
        self.p = p
        self.marge = 0.000001
        if (4*self.a**3 + 27*self.b**2) % self.p == 0:
            print("Deze curve definieert geen groep onder modulo "+str(self.p))
        
    def __str__(self):
        string = "Vergelijking: y^2 = x^3 "
        if self.a == 1:
            string += "+ x "
        elif self.a != 0:
            string += "+ " + str(self.a) + "x "
        if self.b != 0:
            string += "+ " + str(self.b)
        return string
        
    def findStartingPoint(self):
        return
        #priemfactorisatie
        #O(subgroep) | orde(groep)
        #Als niet kleinste subgroep, dan is het grote subgroep
        
    def giveY(self,x):
        #returns positive y
        return math.sqrt(x**3 + self.a*x + self.b)
    
    def points(self): # geeft een lijst met alle punten met gehele waarden die op de curve liggen.
        punten = ["inf"]
        p = self.p
        for x in range(p):
            for y in range(p):
                if (y**2) % p == (x**3 + self.a*x + self.b) % p:
                   punten.append((x,y)) 
        return punten
                
    def __eq__(self,other):
        marge = self.marge
        return abs(self.a - other.a) < marge and abs(self.b - other.b) < marge
        #return self.a == other.a and self.b == other.b

#curve = Elliptic_curve()
#punt_p = Point(curve,1,2)
#punt_q = Point(curve,-7/4,-27/8)