#coding:utf-8

from collections import deque
import os

N = int(raw_input())

grid = []
for i in xrange(N):
    grid_points = list(raw_input())
    grid.append(grid_points)

a, b, c, d = map(int, raw_input().split())

queue = deque([(a, b)])
visited = [[False] * N for _ in xrange(N)]
step = [[0] * N for _ in xrange(N)]
visited[a][b] = True

def is_legal(x, y):
    global N, grid
    return 0 <= x < N and 0 <= y < N and grid[x][y] == '.'

def is_goal(x, y):
    global c, d
    return x == c and y == d

def process(x, y, i, j):
    global queue, visited, step
    if visited[i][j] == False:
        queue.append((i, j))
        step[i][j] = step[x][y] + 1
        visited[i][j] = True

def minstep():
    global queue
    while queue:
        x, y = queue.popleft()
        #up
        i, j = x-1, y
        while is_legal(i, j):
            if is_goal(i, j):
                return step[x][y] + 1
            process(x, y, i, j)
            i -= 1
        #down
        i, j = x+1, y
        while is_legal(i, j):
            if is_goal(i, j):
                return step[x][y] + 1
            process(x, y, i, j)
            i += 1
        #left
        i, j = x, y-1
        while is_legal(i, j):
            if is_goal(i, j):
                return step[x][y] + 1
            process(x, y, i, j)
            j -= 1
        #right
        i, j = x, y+1
        while is_legal(i, j):
            if is_goal(i, j):
                return step[x][y] + 1
            process(x, y, i, j)
            j += 1

print minstep()
