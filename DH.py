import krommen

class DH:
    
    def __init__(self,P,a,b,curve): #P and the curve are public, a and b are secret numbers.
        print("A = P*a = " + str(P*a))
        A = P*a
        print("B = P*b = " + str(P*b))
        B = P*b
        print("Deze worden naar elkaar toe gestuurd")
        print("A*b = " + str(A*b))
        print("B*a = " + str(B*a))
        print("Nu bezitten beide partijen hetzelfde geheime punt:")
        print(str(A*b) + " = " + str(B*a))

            
        
        