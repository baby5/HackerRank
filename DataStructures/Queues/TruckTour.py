#coding:utf-8

from collections import deque

N = int(raw_input())

pump_list = [tuple(map(int, raw_input().split()))  for _ in xrange(N)]

start_index = 0
next_index = 0
queue = deque([pump_list[start_index]])
Sum = 0

while queue:
    next_index = 0 if next_index+1 == N else next_index+1
    
    amount, distance = queue.popleft()
    Sum += amount - distance
    
    if Sum < 0:
        Sum = 0
        start_index = next_index
        queue = deque([pump_list[start_index]])
    else:
        if next_index == start_index:
            print start_index
            break
        else:
            queue.append(pump_list[next_index])
            
        
        
'''
for index in xrange(N):
    pump_index = index
    queue = deque([pump_list[pump_index]])
    carry_amount = 0
    is_circle = False
    
    while queue:
        amount, distance = queue.popleft()
        carry_amount += amount
        
        if carry_amount >= distance:
            carry_amount -= distance
            
            if pump_index+1 == N:
                pump_index = 0
            else:
                pump_index += 1
                if pump_index == index:
                    is_circle = True
                    break
            queue.append(pump_list[pump_index])
    
    if is_circle:
        print index
        break
'''
