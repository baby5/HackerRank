#coding:utf-8

for _ in xrange(input()):
    N = input()

    count = 0
    while N > 1:
        n = 1
        tmp = N
        num = 0
        while tmp > 1:
            tmp >>= 1
            n <<= 1
            num += 1

        if N == n:
            count += num
            break
        else:
            N -= n
            count += 1

    if count % 2 == 0:
        print 'Richard'
    else:
        print 'Louise'
