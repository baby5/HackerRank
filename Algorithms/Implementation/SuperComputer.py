#coding:utf-8
from itertools import combinations

N, M = map(int, raw_input().split())

grid = [list(raw_input()) for _ in xrange(N)]

valid_plus = []

import pdb
for i in xrange(N):
    for j in xrange(M):
        if grid[i][j] == 'B':
            continue       
        
        valid_plus.append(set(tuple([(i, j)])))
        
        poss_plus_list = [(i, j)]
        for k in xrange(1, 8):
            #越界 out of range
            if i-k < 0 or i+k == N or j-k < 0 or j+k == M:
                break
            plus_edges = [(i-k, j), (i+k, j), (i, j-k), (i, j+k)]
            #bad
            if filter(lambda x: grid[x[0]][x[1]] == 'B', plus_edges):
                break
            
            poss_plus_list += plus_edges
            valid_plus.append(set(tuple(poss_plus_list)))


max_size = 1
for set1, set2 in combinations(valid_plus, 2):
    if not (set1 & set2):
        max_size = max(max_size, len(set1)*len(set2))

print max_size
            
