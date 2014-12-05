import math
import time

def no34(limit = 3000000):
    
    shriekdict = {}
    for x in range(10):
        value = math.factorial(x)
        shriekdict.update({str(x): value})


    i = 10 
    answer_list = []
    while i < limit:
        test = 0 
        for j in str(i):
            test += shriekdict[j]
        if test == i:
            answer_list.append(i)

        i += 1
    
    solution = 0
    for a in  answer_list:
        solution += a
    return solution




if __name__ == '__main__':
    start = time.time()
    print no34()
    print '---------------%s--------------' %(time.time() - start)