import krommen
class myclass:
    def __init__(self,value):
        self.value = value
    
    def add(self,other):
        return self.value + other.value
    
    def __str__(self):
        return str(self.value)
    
first = myclass(2)
second = myclass(5)
print(first)
print(second)
print(first.add(second))
print(first)


    def findLine(self,other):
        #lijn vinden y = Qx+R:
            DeltaY = self.y - other.y
            DeltaX = self.x - other.x
            Q = DeltaY/DeltaX 
            R = self.y - Q*self.x
            linelist = [Q,R]
            return linelist
    
    
    
    def findIntersection(self,linelist):
            Q = linelist[0]
            R = linelist[1]
            #snijpunt vinden:
            func = lambda x: x*x*x + Q*Q*x*x + (2*Q*R+self.curve.a)*x + self.curve.b + R*R
            #kansvolle X vinden:
            candidates = Bisection.findAllRoots(func,-100.,1000000.,0.0001)
            for xtry in candidates:
                trypoint = Point(self.curve,xtry,self.curve.giveY(xtry))
                if trypoint == self:
                    # een van de eerste punten gevonden, ga verder
                    continue
                elif trypoint.onCurve():
                    #Yippe dit is hem
                    return trypoint
                # probeer de negatieve y:
                trypoint = Point(self.curve,xtry,-self.curve.giveY(xtry))
                if trypoint == self:
                    # een van de eerste punten gevonden, ga verder
                    continue
                elif trypoint.onCurve():
                    #Yippe dit is hem
                    return trypoint
                else:
                    print('Addition failed, no intersection with E')
                    return None
                            #negatie
            punt = Point(self.curve,self.x,self.y)
        
        #return snijpunt