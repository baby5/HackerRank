#coding:utf-8

t1, t2, n = map(int, raw_input().split())

ar = [t1, t2]

for i in xrange(2, n):
    ar.append(ar[i-2] + ar[i-1]**2)

print ar[n-1]
