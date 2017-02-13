#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    ar = map(int, raw_input().split())

    maxsum = None
    maxar = []

    maxmum = 0
    maxneg = -10 ** 4
    have_positive = 0
    i = 0
    for a in ar:
        i += 1
        if a >= 0:
            if maxsum == None:
                maxsum = a
            else:
                maxsum += a
            
            if i == N:
                maxar.append(maxsum)
            
            have_positive = 1
            maxmum += a
        else:
            if maxsum != None:
                maxar.append(maxsum)
                if a + maxsum <= 0:
                    maxsum = None
                else:
                    maxsum += a
                    
            maxneg = max(maxneg, a)
    
    if maxar:
        print max(maxar),
    elif maxsum:
        print maxsum,
    else:
        print maxneg,

    if have_positive:
        print maxmum
    else:
        print maxneg
