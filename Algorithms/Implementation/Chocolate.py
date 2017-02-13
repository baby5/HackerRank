#coding:utf-8

for _ in xrange(int(raw_input())):
    n, c, m = map(int, raw_input().split())

    count = n / c
    wrapper = count
    while wrapper / m:
        tamp = wrapper / m
        count += tamp
        wrapper = tamp + wrapper%m

    print count
