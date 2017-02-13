#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    b_ar = map(int, raw_input().split())

    lo = 0
    hi = 0

    for i in xrange(1, N):
        l = max(abs(1-b_ar[i-1]) + hi, lo)
        h = max(abs(b_ar[i]-1) + lo, abs(b_ar[i]-b_ar[i-1]) + hi)
        lo, hi = l, h
    print max(lo, hi)
