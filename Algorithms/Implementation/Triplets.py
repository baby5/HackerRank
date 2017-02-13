#coding:utf-8

from collections import deque

n, d = map(int, raw_input().split())
a_list = map(int, raw_input().split())

queue = deque()
count = 0
for a in a_list:
    while queue and a > queue[0][0]:
        queue.popleft()
   
    while queue and a == queue[0][0]:
        cell = queue.popleft()
        if cell[1] == 3:
            count += 1
        else:                 
            queue.append((cell[0]+d, cell[1]+1))

    queue.append((a+d, 2))

print count
