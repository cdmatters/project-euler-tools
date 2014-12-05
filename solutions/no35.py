import primer
import time

start_time = time.time()


def flip(digit):
    dig = digit[-1]
    return dig+(digit[:-1])


submilli = primer.get_primelist(1000000)
basic_set = [False] * 1000000
ind = 1
for i in submilli:
    basic_set[i] = True

for i in xrange(1,1000000, 2):
    if (i/10) % 2 == 0 and (i/10 >0):
        basic_set[i] = False
    elif((i/100) % 2 == 0 )and (i/100 > 0):
        basic_set[i] = False
    elif((i/1000) % 2 == 0 )and (i/1000 > 0):
        basic_set[i] = False
    elif((i/10000) % 2 == 0 )and (i/10000 > 0):
        basic_set[i] = False
    elif((i/100000) % 2 == 0 )and (i/100000 > 0):
        basic_set[i] = False

tester = []
for i in xrange(0,1000000):
    if basic_set[i]:
        tester.append(str(i))

for i in tester:
    j=0
    f = flip(i)
    while j<len(i)-1:
        if f not in tester:
            rid = tester.index(i)
            tester[rid] = '0'
            break
        else:
            f = flip(f)
            j+=1

ans = []
for i in tester:
    if i != '0':
        ans.append(i)


print len(ans), ans


print '---------%ss---------' % (time.time()-start_time)
