from krommenCasper import *

def phi(scalar,punt,lengte = 10):
    return int(bin((punt*scalar).x)[2:lengte+2],2)
c = Elliptic_curve(17,2,2)
p = Point(c,5,1)
print(phi(13,p,3))
print(p)
print(p*2)
print(p*3)
    
    
    
    
    

    
    