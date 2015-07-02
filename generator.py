from krommen import *

class Generator:
 
    def __init__(self, P, Q, seed = 10, trunc = 2):         # seed should be based on time but isn't for convenience
        self.P = P
        self.Q = Q
        if not P.curve == Q.curve:
            print('P and Q not on same curve')
        self.seed = seed
        self.trunc = trunc

    def _phi(self,punt,scalar):
        return (punt*scalar).x

    def _truncate(self,getal):
        return int(str(getal)[:-self.trunc])

    def generate(self): 
        self.seed = self._phi(self.P,self.seed)             # calculation of the next seed
        return self._truncate(self._phi(self.Q,self.seed))  # calculation of the output
