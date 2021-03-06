#coding:utf-8

import heapq as heapq_min

#大小顶堆，0.55s

#如果都是正值，可以用小顶堆保存负值来实现大顶堆
class Heapq_max(object):
    
    def heappush(self, heap, item):
        i = len(heap)
        heap.append(None)

        while i > 0 and heap[(i-1)/2] < item:
            heap[i] = heap[(i-1)/2]
            i = (i-1)/2
        heap[i] = item

    def heappop(self, heap):
        Max = heap[0]
        heap[0] = heap.pop()
        i = 0
        n = len(heap)
        
        while 2*i + 1 < n:
            left = heap[2*i + 1]
            index = 2*i + 1
            
            if 2*i + 2 < n:
                right = heap[2*i + 2]
                if right > left:
                    index = 2*i + 2
            
            if heap[i] < heap[index]:
                heap[i], heap[index] = heap[index], heap[i]
                i = index
            else:
                break
        
        return Max

heapq_max = Heapq_max()

min_heap = []
max_heap = []

n = int(raw_input())
for i in xrange(1, n+1):
    a = int(raw_input())
    if i == 1:
        heapq_min.heappush(min_heap, a)
        
        print min_heap[0] / 1.0
        continue
    
    if len(max_heap) > len(min_heap):
        if a >= max_heap[0]:
            heapq_min.heappush(min_heap, a)
        else:
            temp = heapq_max.heappop(max_heap)
            heapq_min.heappush(min_heap, temp)
            heapq_max.heappush(max_heap, a)
        
    elif len(max_heap) < len(min_heap):
        if a <= min_heap[0]:
            heapq_max.heappush(max_heap, a)
        else:
            temp = heapq_min.heappop(min_heap)
            heapq_max.heappush(max_heap, temp)
            heapq_min.heappush(min_heap, a)
    else:
        if a <= max_heap[0]:
            heapq_max.heappush(max_heap, a)
        else:
            heapq_min.heappush(min_heap, a)
        
    if len(max_heap) == len(min_heap):
        print (max_heap[0] + min_heap[0]) / 2.0
    elif len(max_heap) > len(min_heap):
        print max_heap[0] / 1.0
    else:
        print min_heap[0] / 1.0

'''
#投机解法, 1.3s
import bisect

n = int(raw_input())
a_list = []
for i in xrange(1, n+1):
    a = int(raw_input())

    bisect.insort(a_list, a)
    
    if i % 2 != 0:
        print a_list[i/2] * 1.0
    else:
        print (a_list[i/2-1] + a_list[i/2]) / 2.0
'''
