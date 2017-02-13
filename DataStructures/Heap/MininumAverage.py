#coding:utf-8

from heapq import heappush, heappop
from bisect import insort

N = int(raw_input())

customers = []
for _ in xrange(N):
    customer = map(int, raw_input().split())
    customers.append(customer) 

customers.sort()

waiting_time = 0
current_time = 0
heap = []
i = 0
while 1:
    if i < N and customers[i][0] <= current_time:
        heappush(heap, customers[i][::-1])
        i += 1
    else:
        if len(heap) == 0:
            if i < N:
                current_time = customers[i][0]
                continue
            else:
                break
        
        cook_time, order_time = heappop(heap) 
        current_time += cook_time
        waiting_time += current_time - order_time
    
print waiting_time / N
