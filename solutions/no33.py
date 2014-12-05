

fraction = 4998
chop = None
solution = []




x = 10
y = 11
while x < y:
    y=11
    while y < 99:
         
        fraction = x*100 +y        #print fraction
        #remove duplicates and evaluate WATCH OUT 3 THE SAME

        badmath = ''
        chop = ''
        for f in str(fraction):
            if str(fraction).count(f) >1 :
                chop = f
            else:
                badmath += f

        if len(badmath) == 1:
            badmath+=chop
        elif len(badmath) == 4:
            badmath = 91
            
        try: 
            badfrac =  float(badmath[0])/float(badmath[1])
        except:
            badfrac = 100
        goodfrac = float(fraction/100)/float(fraction%100)


        

        if badfrac == goodfrac and badfrac < 1:
            if not (x%10 == 0 and y%10 == 0):
                print str(fraction/100)+'/'+str(fraction%100), "     ", badfrac
                solution.append(goodfrac)
        y+=1
    x+=1

print solution
pe = 1
for s in solution:
    pe*= s
    print pe


        