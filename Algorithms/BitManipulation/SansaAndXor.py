#coding:utf-8

for _ in xrange(input()):
    N = input()
    ar = map(int, raw_input().split())

    if not N & 1:
        print 0
    else:
        print reduce(lambda x,y: x^y, (ar[i] for i in xrange(0, N, 2)))
