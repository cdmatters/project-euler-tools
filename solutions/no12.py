from primer import Primed
import time

start_time = time.time()


f, i, triangle = 0, 0, 0
while f < 500:
    natural = i +1 
    triangle = triangle + natural

    p = Primed(triangle)
    f = len(p.get_factors())
    i +=1

print p.no, p.factors
print '--------%ss-------'%(time.time() - start_time)

