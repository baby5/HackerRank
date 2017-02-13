#coding:utf-8

n = int(raw_input())
m = int(raw_input())

matrix = []
for _ in xrange(n):
    matrix.append(raw_input().split())

maxmum = 0
region = 0
seen_set = set()

def is_valid(x, y):
    return x > -1 and x < n and y > -1 and y < m


def dfs(cell):
    global region
    seen_set.add(cell)
    region += 1
    a, b = cell

    #简化写法
    for x in [a-1, a, a+1]:
        for y in [b-1, b, b+1]:
            if is_valid(x, y) and matrix[x][y] == '1' and (x, y) not in seen_set:
                dfs((x, y))

    return region

for i in xrange(n):
    for j in xrange(m):
        if matrix[i][j] == '1' and (i, j) not in seen_set:
            maxmum = max(maxmum, dfs((i, j)))
            region = 0

print maxmum


