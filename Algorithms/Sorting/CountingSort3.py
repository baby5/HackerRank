#coding:utf-8

from collections import Counter

n = int(raw_input())
counter = Counter()
for i in xrange(n):
    x, s = raw_input().split()
    counter += Counter([x])

ar = []
pr = 0
for i in xrange(100):
    num = counter.get(str(i), 0)
    ar += [pr + num]
    pr += num

print ' '.join(map(str, ar))
    
    

