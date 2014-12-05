import time
import math

def no25(length = 999):

    fibj = 1
    fibk = 1
    counter = 2

    tops = 10**length
    

    while (fibj / tops) == 0 :
        fibj += fibk
        fibk += fibj
        counter +=2

    #instead of testing twice every time, (both fibj & fibk), test only fibj
    #then check fibk and fib(k-1)


    if fibk/tops != 0:
        counter = counter
    if fibj/tops != 0:
        counter -=  1
    if (fibk-fibj) != 0:
        counter -= 1

    return counter





if __name__ == '__main__':
    start = time.time()
    print no25()
    print '-----------%s-----------' % (time.time() - start)