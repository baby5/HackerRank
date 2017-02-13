#coding:utf-8

Q = int(raw_input())
import pdb

#queries = [raw_input() for _ in xrange(Q)]

heap = [-10 ** 9]
#用set记录元素，实现惰性删除
item_lookup = set()

#for s in queries:
for _ in xrange(Q):
    s = raw_input()
    if s.startswith('1'):
        i = len(heap)
        heap.append(None)
        v = int(s.split()[-1])

        while heap[i/2] > v:
            heap[i] = heap[i/2]
            i /= 2
        heap[i] = v
        item_lookup.add(v)
    elif s.startswith('2'):
        v = int(s.split()[-1])
        item_lookup.discard(v)
        '''
        i = 1
        v = int(s.split()[-1])
        
        #log(n)了，慢的飞起
        while heap[i] != v:
            i += 1

        size = len(heap) - 1
        while i*2 < size:
            if heap[i*2] < heap[i*2+1]:
                heap[i] = heap[i*2]
                i *= 2
            else:
                heap[i] = heap[i*2+1]
                i = i*2 + 1
        
        if i < size:
            heap[i] = heap.pop()
        else:
            heap.pop()
        '''
    elif s.startswith('3'):
        while heap[1] not in item_lookup:
            #最小值已经被惰性删除的话，重新heapify
            i = 1
            size = len(heap) - 1
            while i*2 < size:
                if heap[i*2] < heap[i*2+1]:
                    heap[i] = heap[i*2]
                    i *= 2
                else:
                    heap[i] = heap[i*2+1]
                    i = i*2 + 1
            
            if i < size:
                heap[i] = heap.pop()
            else:
                heap.pop()
        print heap[1]
        
