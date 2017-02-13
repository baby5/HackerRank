#coding:utf-8

import math

T = int(raw_input())
for _ in xrange(T):
    A, B = map(int, raw_input().split())
    count = 0

    sqr = math.floor(math.sqrt(A))
    if sqr ** 2 == A:
        count += 1
    sqr += 1
    
    while sqr**2 <= B:
        count += 1
        sqr += 1

    print count
        
