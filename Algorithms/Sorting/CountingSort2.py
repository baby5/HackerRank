#coding:utf-8

from collections import Counter

n = int(raw_input())
counter = Counter(raw_input().split())

ar = []
for i in xrange(100):
    ar += [str(i)] * counter.get(str(i), 0)

print ' '.join(ar)
