#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N, K = map(int, raw_input().split())
    a_list = map(int, raw_input().split())
    
    count = 0
    for a in a_list:
        if a <= 0:
            count += 1
    
    if count >= K:
        print 'NO'
    else:
        print 'YES'
