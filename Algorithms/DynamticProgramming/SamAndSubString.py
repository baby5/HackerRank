#coding:utf-8

N = raw_input()
l = len(N)
mod = 10**9 + 7
r = 0
f = 1

for i in xrange(l-1, -1, -1):
    r += (int(N[i]) * f * (i+1)) % mod
    f = (f*10 + 1) % mod

print r % mod
