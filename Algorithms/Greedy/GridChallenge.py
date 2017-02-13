#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    grid = [sorted(raw_input())  for _ in xrange(N)]

    is_yes = True
    for j in xrange(len(grid[0])):
        for i in xrange(1, N):
            if grid[i][j] < grid[i-1][j]:
                is_yes = False
                break
        if not is_yes:
            break

    if is_yes:
        print 'YES'
    else:
        print 'NO'
        
