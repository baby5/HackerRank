#coding:utf-8

import heapq
import pdb
N, K = map(int, raw_input().split())

heap = map(int, raw_input().split())
heapq.heapify(heap)

opera_num = 0
while 1:
    if len(heap) >= 2:
        if heap[0] >= K:
            print opera_num
            break
        
        least = heapq.heappop(heap)
        second = heapq.heappop(heap)

        sweetness = least + 2*second
        heapq.heappush(heap, sweetness)
    
        opera_num += 1
    else:
        if heap[0] >= K:
            print opera_num
        else:
            print -1
        break


