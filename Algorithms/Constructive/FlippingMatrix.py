#coding:utf-8

for _ in xrange(int(raw_input())):
    n = int(raw_input())

    matrix = [map(int, raw_input().split())
         for __ in xrange(2*n)
    ]
    
    maximum = 0
    for i in xrange(n):
        for j in xrange(n):
            maximum += max(
                matrix[i][j],
                matrix[i][2*n-1-j],
                matrix[2*n-1-i][j],
                matrix[2*n-1-i][2*n-1-j],
            )

    print maximum
