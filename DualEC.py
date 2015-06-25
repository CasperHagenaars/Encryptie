from krommenCasper import *

class Generator:
    
    def __init__(self,POINT_P,POINT_Q,INT_seed,INT_trunclen = 10):
        self.POINT_P = POINT_P
        self.POINT_Q = POINT_Q
        if not self.POINT_P.curve == self.POINT_Q.curve:
            print('Bad ECPRNG: P and Q not on same curve')
        self.INT_seed = INT_seed
        self.INT_trunclen = INT_trunclen
        
    def phi(self,scalar,punt):
        return int(bin((punt*scalar).x)[2:self.INT_trunclen+2],2)
        
    def _getNextSeed(self):
        return self.phi(self.INT_seed,self.POINT_P)
        
    def _getPRN(self):
        return self.phi(self.INT_seed,self.POINT_Q)
        
    def getNextPRN(self):
        self.INT_seed = self._getNextSeed()
        while len(str(self.INT_seed)) < self.INT_trunclen:
            toevoeging = str(self._getNextSeed())
            self.INT_seed = str(self.INT_seed)
            self.INT_seed += toevoeging
            self.INT_seed = int(self.INT_seed)
        return self._getPRN()
        
    
        