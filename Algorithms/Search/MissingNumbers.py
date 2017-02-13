#coding:utf-8

A = [0] * 10001
B = [0] * 10001

n = raw_input()
for x in map(int, raw_input().split()):
    A[x] += 1

m = raw_input()
for x in map(int, raw_input().split()):
    B[x] += 1

for i in xrange(1, 10001):
    if B[i] > A[i]:
        print i,
'''
#python版
from collections import Counter

n = int(raw_input())
counter_a = Counter(raw_input().split())

m = int(raw_input())
counter_b = Counter(raw_input().split())

counter = counter_b - counter_a
for key in sorted(counter.iterkeys(), key=lambda x: int(x)):
        print key,
'''