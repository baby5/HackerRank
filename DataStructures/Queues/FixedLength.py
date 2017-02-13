#coding:utf-8

from collections import deque
import pdb

n, q = map(int, raw_input().split())

A_list = map(int, raw_input().split())

d_list = [int(raw_input()) for _ in xrange(q)]

for d in d_list:
    #双端队列
    dq = deque()
    best = None
    
    for i in xrange(n):
        #保证队列头是最大值
        while dq and A_list(dq[-1]) < A_list[i]:
            dq.pop()
        dq.append(i)
        #如果队列头出"窗口"，则要出列
        while dq and dq[0] <= i - d:
            dq.popleft()
        #"窗口"移动前要记录最大值
        if i >= d - 1:
            assert dq
            best = min(best, a[dq[0]]) if not best else a[dq[0]]

    print best
'''
for d in d_list:
    queue = deque([A_list[0]])
    max_queue = deque([A_list[0]])
    
    max_list = []
    for a in A_list[1:]:
        queue.append(a)
        if len(queue) > d:
            #pdb.set_trace()
            temp = queue.popleft()
            max_list.append(max_queue[0])
            
            if max_queue[0] == temp:
                max_queue.popleft()
         
        if max_queue and max_queue[-1] >= a:
            max_queue.append(a)
        else:
            while max_queue and max_queue[-1] < a:
                max_queue.pop()
            max_queue.append(a)
    
    max_list.append(max_queue[0]) 
    print min(max_list)
'''

'''
for _ in xrange(q):
    d = int(raw_input())
    out_list = []
    
    for i in xrange(n):
        left = i
        if i+d > n:
            break
        right = i + d
        part = slice(left, right)
        
        out_list.append(max(A_list[part]))
    
    print min(out_list)
'''            
    
