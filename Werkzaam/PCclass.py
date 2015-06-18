import krommen

class PC:
    
    def __init__(self,naam,kromme,punt_public,getal_geheim):
        self.naam = naam
        self.kromme = kromme
        self.punt_public = punt_public
        self.getal_geheim = getal_geheim
        
    def __str__(self):
        prstr = 'PC '+str(self.naam)+' heeft: [E = '+str(self.kromme)+' , p = '+str(self.punt_public)+' , geheim getal = '+str(self.getal_geheim)+']'
        return prstr
        
        
    def stringToInt(self,STR_message):
        # maakt van een string een array ints (ASCII waarden)
        return [ord(i) for i in STR_message]
        
    def askForPoint(self,other):
        print('Public point: '+str(other.punt_public))
        print('Other secret number: '+str(other.getal_geheim))
        nBp =  other.punt_public * other.getal_geheim # vraag van de ander nB * afgesproken punt 
        print('returning nBp : '+str(nBp))
        return nBp
        
        
    def messageToCode(self,STR_message,other):
        # maakt van een zin (string) een versleutelde code (int)
        INT_ARR_toSend = self.stringToInt(STR_message) # text als ASCII code
        print('worked')
        nBp = self.askForPoint(other)
        print('nBp : '+str(nBp))
        POINT_key = self.getal_geheim * nBp # bereken nA*nB*p (alleen voor self en other bekend)
        print('worked here')
        print(POINT_key)
        POINT_ARR_encryption = [POINT_key*i for i in INT_ARR_toSend]
        print('holy shit!')
        ## vermenigvuldig de INT_ARR
        return POINT_ARR_encryption

            
        
        