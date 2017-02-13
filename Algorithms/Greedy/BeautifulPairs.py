#coding:utf-8

from collections import Counter

N = int(raw_input())
A = Counter(map(int, raw_input().split()))
B = Counter(map(int, raw_input().split()))

count = sum([value for value in (A&B).values()])
if A - B:
    count += 1
else:
    count -= 1

print count
