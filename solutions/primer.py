#primer.py contains classes for PE prime problems

import math

class Primed(object):

    def __init__(self, raw_no):
        self.no  = int(raw_no)
        self.primes = []
        self.factors = []
        self.index_note = []

        self.get_primes()

       

    def get_primes(self):
        #populate the primes of the target number
        tally = self.no
        self.primes = []
        #multiples of 2
        while tally % 2 == 0:
            tally = tally/2
            self.primes.append(2)
        #odd primes
        i = 3
        while tally > 1 and i <= math.sqrt(tally):
            if tally % i == 0:
                tally = tally/i
                self.primes.append(i)
            else:
                i +=2
        if tally > 1:
            self.primes.append(tally)

        return self.primes

    def get_factors(self):
        #populate all factors of the number from primes
        
        i=0
        while i < len(self.primes):
            container=[]
            for j in self.factors:
                if j*self.primes[i] not in self.factors:
                    container.append(j*self.primes[i])
            if self.primes[i] not in self.factors:
                self.factors.append(self.primes[i])
            self.factors.extend(container)
        #how does the not in function work? because the data is sorted so it could be faster to code own test
            i+=1
        self.factors.sort()
        return self.factors

        

def get_primelist(upto):
    #returns a list of all the primes upto the input number
    sieve = [False] * (upto + 1)

    storeme = []     
    
    for i in xrange(4, upto + 1, 2):     #every multiple of 2 now =True
        sieve[i] = True  
    for i in xrange(3, int(pow(upto, 0.5)) + 1, 2):  #this loop flips multiples of i to True
        if not sieve[i]:                             #after starting at 3, it starts at next false
            for x in xrange(i*i, upto + 1, i):          #the multiples, start at i*2, as all earlier ones crossed out already
                sieve[x] = True                     #it only needs to check up to root'upto'                                         #every other false beyond MUST be prime.
    for i in xrange( 2, upto + 1):
        if not sieve[i]:
            storeme.append(i)                       #this creates a list of primes
    return storeme




if __name__ == '__main__':
    try:
        p = Primed(int(raw_input("number to operate on...:")))
        if raw_input("do you want primes?").lower() == ('y' or 'yes'):
            print p.primes
        elif raw_input('do you want factors').lower() == ('y' or 'yes'):
            print p.get_factors()
    except:
        get_primelist(int(raw_input('testing primelist fn: print primes up to...')))


