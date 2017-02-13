#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    ar = map(int, raw_input().split())

    k_ar = [0] * N
    for i in xrange(N):
        for j in xrange(N):
            if ar[j] >= ar[i]:
                k_ar[i] += 1
    
    print '%.2f' % ((N+1) * sum([1.0/(k+1) for k in k_ar]))
