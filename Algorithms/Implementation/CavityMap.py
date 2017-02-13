# coding:utf-8

n = int(raw_input())
Map = [map(int, list(raw_input())) for _ in xrange(n)]
c = len(Map[0])

if n <= 2 or c <= 2:
    for row in Map:
        print ''.join(map(str, row))
else:
    for i in xrange(1, n-1):
        for j in xrange(1, c-1):
            if (Map[i-1][j] != 'X' and
                Map[i+1][j] != 'X' and
                Map[i][j-1] != 'X' and
                Map[i][j+1] != 'X' and
                Map[i][j] > Map[i-1][j] and
                Map[i][j] > Map[i+1][j] and
                Map[i][j] > Map[i][j-1] and
                Map[i][j] > Map[i][j+1]):
                Map[i][j] = 'X'
    for row in Map:
        print ''.join(map(str, row))
