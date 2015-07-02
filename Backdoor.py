import generator
import krommen

class Backdoor:
    def __init__(self,generator,output,d):
        try:
            self.r1 = output[0]
            self.r2 = output[1]
        except:
            print('Backdoor needs at least two output states [out1,out2]')

        self.P = generator.P
        self.Q = generator.Q
        self.d = d
        
    def _predictNext(self, output, trunc = 2):              # calculates the next number based on a current, untruncated, output
        Qs = self.P.curve.findY(output)
        self.seed = (Qs*self.d).x
        output = self.Q*self.seed
        return int(str(output.x)[:-trunc])
    
    def findSeed(self,trunc = 2):                           # tries to find the seed for all possibilties created by the truncation
        r1 = int(str(self.r1) + ("0"*trunc))
        for _ in range(10**trunc):
            if self._predictNext(r1,trunc) == self.r2:
                return (self.seed)
            r1 += 1
        return None