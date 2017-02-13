#coding:utf-8

#T = int(raw_input())

#for _ in xrange(T):
#    n = int(raw_input())
#    array = map(lambda x: [int(x), 0], raw_input().split())
with open('data', 'r') as fIn:
    n = 99928
    array = map(lambda x: [int(x), 0], fIn.read().strip().split())

    is_chaos = False
    count = 0
    for i in xrange(n):
        if array[i][0] > i+1:
            array[i][1] += 1
            if array[i][1] > 2:
                is_chaos = True
            else:
                for j in xrange(i+1, n):
                    if array[j][0] > i+1:
                        array[j][1] += 1
                    elif array[j][0] == i+1:
                        array.insert(i, array.pop(j))
                        break
            count += j-i

        if is_chaos:
            print 'Too chaotic'
            break
    if not is_chaos:
        print count 
'''
    count = 0
    is_chaos = False
    while 1:
        for i in xrange(n-1):
             if array[i+1] < array[i]:
                if array[i][1] + 1 > 2:
                    is_chaos = True
                    break
                array[i][1] += 1
                array[i], array[i+1] = array[i+1], array[i]
                count += 1
                is_swaped = True
        
        if is_chaos:
            break
        elif is_swaped:
            is_swaped = False
        else:
            break

    if is_chaos:
        print 'Too chaotic'
    else:
        print count
'''
