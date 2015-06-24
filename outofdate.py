import math
#import Bisection

class Point:
    def __init__(self,curve,x,y):
        self.x = x
        self.y = y
        self.curve = curve
        self.onCurve()
        #if not self.onCurve():
            #print("Punt ("+str(x)+","+str(y)+") niet op kromme")
        #else:
            #print("Wel op kromme")
    
    def __str__(self):
        return str("(x,y) = ("+str(self.x)+","+str(self.y)+")")
            
    def __eq__(self,other):
        if other == None:
            return None
        marge = 0.00001
        return (math.fabs(self.x - other.x) < marge and math.fabs(self.y - other.y) < marge)
        
    def double(self):
        s = (3*self.x*self.x + self.curve.a) /float(2*self.y) #mist mod p
        xr = s*s - 2*self.x # mod p
        yr = self.y + s*(xr-self.x)
        rtpoint = Point(self.curve,xr,-yr)
        return rtpoint
        
#        2P = R where 

#s = (3xP2 + a) / (2yP ) mod p 

#xR = s2 - 2xP mod p and yR = -yP + s(xP - xR) mod p
        
    def __add__(self,other):
        #print('Adding '+str(self)+' to '+str(other))
        if self == other:
            return self.double()
        else:
            DeltaY = other.y - self.y
            DeltaX = other.x - self.x
            if DeltaX == 0:
                print("delen door 0")
                return None
                ## we hebben betere foutmelding hiervoor nodig
            Lambda = (DeltaY/DeltaX) % self.curve.p 
            x_new = Lambda*Lambda - self.x - other.x
            y_new = Lambda*(x_new - self.x) + self.y
            return Point(self.curve,x_new % self.curve.p,-y_new % self.curve.p)
            
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
            POINT_currentdouble = POINT_currentdouble.double()
        return POINT_answer
                
            
        
    def __mul__(self,n):
        return self.mul(n)

    def __neg__(self):
        self.y *= -1
        return self

    def __sub__(self,other):
        return self + (-other)
    
    def onCurve(self):
        marge = 0.0001
        return  math.fabs(self.x**3 + self.curve.a*self.x + self.curve.b - self.y*self.y) < marge
            
class Elliptic_curve:
    def __init__(self,p=17, a=2,b=2):
        self.a = a
        self.b = b
        self.p = p
        
    def __str__(self):
        string = "Vergelijking: y^2 = x^3 + " + str(self.a) + "x + " + str(self.b)
        return string
        
    def points(self):
        punten = []
        p = self.p
        for x in range(p):
            for y in range(p):
                if (y**2 % p) == (x**3+x) % p:
                   punten.append((x,y)) 
        return punten
        
    def giveY(self,x):
        #returns positive y
        return math.sqrt(x**3 + self.a*x + self.b)
    
                
    def __eq__(self,other):
        marge = 0.000001
        return abs(self.a-other.a) < marge and abs(self.b-other.b) < marge
        #return self.a == other.a and self.b == other.b

#curve = Elliptic_curve()
#punt_p = Point(curve,1,2)
#punt_q = Point(curve,-7/4,-27/8)