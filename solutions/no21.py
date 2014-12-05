import primer
import time

def no21(x=10000):

    check_list = []
    finale= []
    i = 2
    while i < x:
        p = primer.Primed(i)
        p.get_factors()
        amic = 1

        p.factors.pop(-1) 
        for f in p.factors:
            amic+=f

        check_list.append((i, amic))
        i+=1


    for j in check_list:
        if j[1] < x:
            if j[0] == check_list[j[1]-2][1]:
                finale.append(j)

    answer = 0
    for k in finale:
        if k[0] != k[1]:
            answer += k[0]

    return answer



if __name__ == '__main__':
    start = time.time()
    print no21()
    print '------------- %ss -------------' %(time.time() - start)


