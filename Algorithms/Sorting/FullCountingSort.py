#coding:utf-8

n = int(raw_input())
counter = [0] * 100
strings = [[] for i in xrange(100)]

for _ in xrange(n):
    x, s = raw_input().split()
    x = int(x)
    s = s if _ >= n/2 else '-'
    counter[x] += 1
    strings[x].append(s)

for i in xrange(100):
    num = counter[i]
    for j in xrange(num):
        print strings[i][j],

