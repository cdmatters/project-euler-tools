import time
import math

def no30(x=5):
    
    listed = []
    i = 2
    while i < 1000000: 
        string = str(i)
        test = 0 
        for j in string:
            test += math.pow(int(j), x)
        if i == test:
            listed.append(i)
        i+=1

        answer = 0
    for l in listed:
        answer += l
    return answer


if __name__ == '__main__':
    start = time.time()
    print no30()
    print '------------- %ss -------------' %(time.time() - start)

