import math
from fractions import gcd

class Point:
    def __init__(self, curve, x, y, inf = False, force = False):
        self.marge = curve.marge                        # marge determined once in curve
        self.x = x
        self.y = y
        self.curve = curve
        self.inf = inf                                  # zero-point/point at infinity
        if self.x == 0 and self.y == 0:                 # for safety reasons
            self.inf = True
        if not self._onCurve():                         # print warning was useful during development, but is frequently called while the behaviour is intended. 
            #print("Point (" + str(x) + "," + str(y) + ") is not on the curve")
            return None
            
    def __str__(self):
        return str("(" + str(self.x) + "," + str(self.y) + ")")
            
    def __eq__(self, other):
        if other == None:
            return False
        if other.inf == True and self.inf == True:
            return True
        elif other.inf == True or self.inf == True:
            return False
        else:
            marge = self.marge
            return (math.fabs(self.x - other.x) < marge and math.fabs(self.y - other.y) < marge)

    def _findInverse(self, n, p = None):                # use Euclidean algorithm ( 1 = ninv * n + x * p ) to get ninv
        if p == None:
            p = self.curve.p
        n = n % p   
        if n == 0:
            print('Error: Inverse of non invertible n = 0 mod p called. Continue with 7')
            return 7
        if n == 1:
            print('Warning: Inverse of 1 called. Returning 1')
            return 1
        oldoldn = 0
        oldn = 1
        oldoldextra = 1
        oldextra = 0
        big = p
        small = n
        while small > 1:                                # Euclid Algorithm
            q = big//small                              # get quotient
            remainder = big % small
            big = small
            small = remainder
            ninv = oldoldn - q*oldn
            oldoldn = oldn
            oldn = ninv
            nextra = oldoldextra - q*oldextra
            oldoldextra = oldextra
            oldextra = nextra
        if small == 0:
            print('Error: Euclidean Algorithm called on n,p with gcd(n,p) != 1. Expect bugs')
            print(big)
        ninv = ninv % p
        return ninv
            
        
        
           
    def __add__(self, other):                           # defines addition for integers on curve over Fp, where p is prime
        if self.inf == True:                            # checks if it is zero
            return other
        if other.inf == True:
            return self
        if self == other:
            xp = self.x
            yp = self.y
            if yp == 0:
                return Point(self.curve, 0, 0, True)
            a = self.curve.a
            p = self.curve.p
            if not (type(xp) == int and type(yp) == int):
                print('Error detected. Trying to double point with non integer x')
                print("type(x) = "+ str(type(xp))+ ", type(y): " + str(type(yp)))
            t = 3*xp**2 + a # teller
            n = 2*yp # noemer
            ninv = self._findInverse(n)                 # s has to be integer, so we use s = ninv*t, which defines 'modulo dividing'
            s = (t * ninv) % p
            xr = (s**2 - 2*xp) % p
            yr = (-yp + s*(xp - xr)) % p
            return Point(self.curve, xr, yr)
        else:                                           # if points are dinstinct
            p = self.curve.p
            xp = self.x
            xq = other.x
            yp = self.y
            yq = other.y
            t = yq - yp
            n = xq - xp
            if n == 0:                                  # same x-value means inverse
                return Point(self.curve, 0, 0, True)
            ninv = self._findInverse(n)
            s = (t*ninv) % p                            # guarantees s to be a integer
            xr = (s*s - xp - xq) % p
            yr = (s*(xp - xr) - yp) % p
            return Point(self.curve, xr, yr)
            
    def __mul__(self, scalar):
        if self.inf == True:
            return self
        if not (isinstance(scalar, int)):
            print('Wrong type of multiplication')
            return None
        binary = bin(scalar)[2:]                        # takes a integer to binary form
        ans = None                                      # ANSwer which will be returned. May change at each iteration of loop
        cpot = self                                     # Current Power Of Two starting at 2^0*p
        for bitnr in range(len(binary) - 1, -1, -1):    # go through starting at least significant bit
            val = binary[bitnr]                         # VALue of bit number: bitnr
            if val == '1':
                if ans == None:                         # ans is None until the first 1 is found
                    ans = cpot
                else:
                    ans += cpot
            cpot += cpot
        return ans

    def __neg__(self):
        if self.inf == True:
            return self
        ry = -self.y % self.curve.p
        return Point(self.curve, self.x, ry) 
        
    def __sub__(self, other):
        return self + -other
    
    def _onCurve(self):
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
            #print(str(lhs) + ' != ' + str(rhs))        # 
            return False
        
    def findOrder(self):                                # find the order of E(p)
        p = self.curve.p
        P = self
        begin = int(p + 1 - 2*math.sqrt(p))             # boundaries according to Hasse's theorem
        end  = int(p + 1 + 2*math.sqrt(p))
        newp = P*(begin)
        for n in range(begin,end):
            newp += P
            if newp.inf == True:
                return (n+1)
        print("No order found")
        return None
        
    def createBackdoor(self,e):                         # find a d such that P = Q*d, when Q = P*e
        order = self.findOrder()
        if order == None:
            print("findOrder called but order is None")
            return None
        if gcd(e,order) != 1:
            print("There is no d such that P = Q*d")
            return None
        return self._findInverse(e,order)
    
            
class EllipticCurve:
    def __init__(self, p = 17, a = 2, b = 2):
        self.a = a
        self.b = b
        self.p = p
        self.marge = 0.000001
        if (4*a**3 + 27*b**2) % p == 0:
            print("This curve doesn't define a group under mod " + str(p))
        
    def __str__(self):                                  # prints equation of the elliptic curve
        string = "Equations: y^2 = x^3 "
        if self.a == 1:
            string += "+ x "
        elif self.a != 0:
            string += "+ " + str(self.a) + "x "
        if self.b != 0:
            string += "+ " + str(self.b)
        return string

    def __eq__(self, other):
        return abs(self.a - other.a) < self.marge and abs(self.b - other.b) < self.marge

    def _power(self, base, power):                      # faster method to calculate base**power
        binary = bin(power)[2:]    
        cpot = base
        ans = None                                      
        for bitnr in range(len(binary) - 1, -1, -1):    
            val = binary[bitnr]
            if val == '1':
                if ans == None:                         
                    ans = cpot
                else:
                    ans *= cpot
                    ans %= self.p
            cpot *= cpot
            cpot %= self.p
        return ans
        
    def findY(self,x):                                  # finding the y-coordinate given an x-coordindate
        p = self.p
        a = self.a
        b = self.b
        rhs = (x**3 + a*x + b) % p
        y = self._power(rhs,int((p+1)/4)) % p          
        return Point(self, x, y, False)