import time
import primer


def no43(x = 10):
    #going to build our pandigit list using the problems specs
    #by realtime trimming 'panlist' w conditions, speed up process.
    #start by generating pandigits for 3 digits (0-9)

    criteria = [2,3,5,7,11,13,17]

    plist = pandigital()
    store= []
    sweetiebox = range(x)



    while criteria:
        divcheck = []
        for p in plist:
            if (p%1000) % criteria[0] == 0:
                divcheck.append(p)
        plist = divcheck
        criteria.pop(0)

        for i in plist:  
            sweetiebox = range(x)
            
            pickt = list(str(i))
            pickt.sort(reverse = True)
            
            for j in pickt:  
                sweetiebox.pop(int(j))  
            for k in sweetiebox:
                store.append(i*10 + k)

        plist = store
        store = []

    answer = 0     #now just need to rearrange last digit to first for PE answer
    for j in plist:

        spare = j%10
        answer+= (spare*(10**9))+(j/10) 
    return answer




def pandigital(x=10, length = 3):
    #generate pandigital numbers, fun function.
    #works by picking sweets out of a jar.
    pandigital = [0]
    store = []
    sweetiebox = range(x)
    while len(sweetiebox)>x-length+1:

        for i in pandigital:  
            sweetiebox = range(x)
            
            pickt = list(str(i))
            pickt.sort(reverse = True)
            
            for j in pickt:  
                sweetiebox.pop(int(j))  
            for k in sweetiebox:
                store.append(i*10 + k)

        pandigital = store
        store = []
    return pandigital



if __name__ == '__main__':
	start = time.time()
	print no43()
	print '-----------%s------------' %(time.time()- start)


