#coding:utf-8

for _ in xrange(input()):
    print 2 ** 32 - input() - 1
    print input() ^ (2**32 - 1)
