#coding:utf-8

T = int(raw_input())

def dfs(cell, count, grid, N, M):
    global Count, seen
    x, y = cell
    if grid[x][y] == '*':
        Count = count
        return
    seen.add((x, y))

    directions = []
    #up
    if x>0 and (x-1, y) not in seen and grid[x-1][y] != 'X':
        directions.append((x-1, y))

    #down
    if x<N-1 and (x+1, y) not in seen and grid[x+1][y] != 'X':
        directions.append((x+1, y))

    #left
    if y>0 and (x, y-1) not in seen and grid[x][y-1] != 'X':
        directions.append((x, y-1))

    #right
    if y<M-1 and (x, y+1) not in seen and grid[x][y+1] != 'X':
        directions.append((x, y+1))

    if len(directions) == 1:
        dfs(directions[0], count, grid, N, M)
    else:
        count += 1
        for cell in directions:
            dfs(cell, count, grid, N, M)

for _ in xrange(T):
    N, M = map(int, raw_input().split())
    grid = []
    x, y = None, None
    for i in xrange(N):
        s = raw_input()
        grid.append(s)
        if 'M' in s:
            x, y = i, s.index('M')
    K = int(raw_input())

    Count = 0
    seen = set()
    dfs((x, y), 0, grid, N, M)
    if Count == K:
        print 'Impressed'
    else:
        print 'Oops!'
