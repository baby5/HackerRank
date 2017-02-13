#!/usr/bin/env python
#coding:utf-8

N, M = map(int, raw_input().split())
ar = map(int, raw_input().split())

table = [[0]*N for _ in xrange(M)]
coin = ar[0]
for i in xrange(N):
    if (i+1) % coin == 0:
        table[0][i] = 1

for i in xrange(1, M):
    coin = ar[i]
    for j in xrange(N):
        if j+1 < coin:
            table[i][j] = table[i-1][j]
        elif j+1 == coin:
            table[i][j] = table[i-1][j] + 1
        else:
            table[i][j] = table[i-1][j] + table[i][j-coin]

print table[M-1][N-1]
