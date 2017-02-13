#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    
    string = ''
    while N:
        if N % 3 == 0:
            string = '5'*N + string
            break
        else:
            if N >= 5:
                string = '3'*5 + string
                N -= 5
            else:
                string = '-1'
                break
    print string

