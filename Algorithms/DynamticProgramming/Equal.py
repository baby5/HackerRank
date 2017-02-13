#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    ar = sorted(map(int, raw_input().split()))
   
    count = 0
    dis = 0
    start = 1

    if N >= 3 and ((ar[1]-ar[0]) % 5 == 3 or (ar[1]-ar[0]) % 5 == 4) and ar[1] == ar[2]:
        tamp = ar[2]
        count = ((ar[1]-ar[0])/5 + 1) * 2 + 1
        if ar[1]-ar[0] % 5 == 4:
            dis = 5*count - 4
            ar[2] = dis
        elif ar[1]-ar[0] % 5 == 3:
            dis = 5*count - 3
            ar[2] = dis
        start = 3
        
        if N > 4 and ((ar[3] - ar[1]) % 5 != 0 or (ar[4] - ar[1]) % 5 != 0):
            count, dis, start = 0, 0, 1
            ar[2] = tamp

    for i in xrange(start, N):
        dis += ar[i] - ar[i-1]
       
        a = dis / 5
        b = (dis - 5*a) / 2
        c = dis - 5*a - 2*b
    
        count += a + b + c
    
    print count
