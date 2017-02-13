#coding:utf-8

from collections import Counter

n = int(raw_input())
counter = Counter(raw_input().split())

print ' '.join(map(str, [counter.get(str(i), '0') for i in xrange(100)]))
