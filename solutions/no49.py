import primer
import time
start_time = time.time()


def seriestester(listed):
    test = []
    collectr = []
    miniresult = []
    megaresult = []
    for a in listed:
        for b in listed:
            if b-a>0:
                test.append(b-a)
                collectr.append((b-a, b, a) )
    test.sort()
    collectr.sort()

    key = 0

    for c in collectr:
        '''        if c[0] == 3330:
            print c'''
        if c[0] == key:
            miniresult.extend([c[1],c[2]])
        else:
            
            if len(miniresult)>2:
                megaresult.append((miniresult, key))
            miniresult = [c[1],c[2]]
            
        key = c[0]

    
    if megaresult:
        for m in megaresult:
            m[0].sort()
            if m[0][1] == m[0][2]:
                       #would be nice to generalise this for internal pairs.., 
                return ((m[0][0],m[0][1],m[0][3]), len(m[0])-1, m[1])  #ie if list was 6 long not 4
    else:
        pass

                    






plist = primer.get_primelist(10000)

compere = []

for p in plist:
   l = list(str(p))
   l.sort()
   j = ''.join(l)
   compere.append(j)

i, magick = 0, []

while i < len(compere):
    c = compere.count(compere[i])
    if c > 3 :
        magick.append((compere[i], plist[i]))    
    i+=1

magick.sort()
magick.append('stop')

key, mlist, majorlist = '', [], []
for m in magick:
    if key == m[0]:
        mlist.append(m[1])
    else:
        majorlist.append(mlist)
        mlist = []
        mlist.append(m[1])
    key = m[0]

majorlist.pop(0)


for alist in majorlist:
    y = seriestester(alist)
    pe = ''
    if y:
        for st in y[0]:
            pe += str(st)
        print pe, y







print '----------%ss-----------' %(time.time() - start_time)