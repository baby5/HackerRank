#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    A = map(int, raw_input().split())

    left = 0
    right = sum(A)

    for a in A:
        right -= a

        if left == right:
            print 'YES'
            break
        elif left > right:
            print 'NO'
            break
            
        left += a