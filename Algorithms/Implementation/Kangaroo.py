#coding:utf-8

x1, v1, x2, v2 = map(int, raw_input().split())

if x1 < x2:
    if v1 > v2:
        #相对速度
        v = v1 - v2
        x = x2 - x1
        if x % v == 0:
            print 'YES'
        else:
            print 'NO'
        '''
        #笨笨的
        while x1 < x2:
            x1 += v1
            x2 += v2
        if x1 == x2:
            print 'YES'
        else:
            print 'NO'
        '''
    else:
        print 'NO'
elif x1 > x2:
    if v1 < v2:
        v = v2 - v1
        x = x1 - x2
        if x % v == 0:
            print 'YES'
        else:
            print 'NO'
    else:
        print 'NO'
else:
    if v1 == v2:
        print 'YES'
    else:
        print 'NO'
