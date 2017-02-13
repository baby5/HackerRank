#coding:utf-8

N = int(raw_input())
K = int(raw_input())

ar = []
for _ in xrange(N):
    ar.append(int(raw_input()))
ar.sort()

minmum = 10 ** 9
for i in xrange(K-1, N):
    minmum = min(minmum, ar[i]-ar[i-K+1])

print minmum
