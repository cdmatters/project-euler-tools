import primer
import time
start_time = time.time()


i = 1
a= primer.Primed(2)
b= primer.Primed(3)
c= primer.Primed(4)
d= primer.Primed(5)
switch = [True,True,True,True]


while i:
    if i%4 == 1:
        a = primer.Primed(i)
        auniq = list(set(a.primes))
        if len(auniq) != 4:
            switch[0] = False
        else:
            switch[0] = True
    elif i%4 == 2:
        b = primer.Primed(i)
        buniq = list(set(b.primes))
        if len(buniq) !=4:
            switch[1] = False
        else:
            switch[1] = True
    elif i%4 == 3:
        c = primer.Primed(i)
        cuniq = list(set(c.primes))
        if len(cuniq)!=4:
            switch[2] = False
        else:
            switch[2] = True
    elif i%4 == 0:
        d = primer.Primed(i)
        duniq = list(set(d.primes))
        if len(duniq)!=4:
            switch[3] = False
        else:
            switch[3] = True

    if switch != [True, True, True, True]:
        i +=1
    else:


        print  a.no,b.no,c.no,d.no
        print auniq, buniq, cuniq, duniq
        break  

        i+=1


print '----------%ss----------' %(time.time()-start_time)
