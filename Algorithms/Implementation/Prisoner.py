#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N, M, S = map(int, raw_input().split())

    mod = M % N 
    S = S + mod - 1
    if S > N:
        S = S - N
    if S == 0:
        S = N
    '''
    #大数循环直接时间爆炸
    for i in xrange(mod):
        if S == N:
            S = 0
        S += i
    '''
    print S
