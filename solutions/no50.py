import primer
import time 

start_time = time.time()

plist = primer.get_primelist(1000000)

print len(plist)

winner = 0
index = 1
bingo = 0
while plist: 
    counter = 0
      
    for i in plist:
        counter = counter + i
        if index % 2 == 0 and index > 0 :
            if counter in plist[bingo:]:
                if index+1 > winner:
                    winner = index+1
                    print counter, winner, plist[0]
                bingo = plist.index(counter)
        if counter > 1000000:

            break
        index+=1

    plist.pop(0)
    bingo -=1
    index = 0

    
















print '------------%ss------------' %(time.time()-start_time)