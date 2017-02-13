#coding:utf-8

from collections import deque
import pdb
import time

Q = int(raw_input())

#BFS，真的好
for _ in xrange(Q):
    N = int(raw_input())
    queue = deque([(N, 0)])
    factor_set = set()
    
    while queue:
        pdb.set_trace()
        N, move = queue.popleft()
        if N == 0:
            print move
            break
         
        factors = [N/i for i in xrange(int(N ** 0.5), 1, -1) if N%i == 0]
        for factor in factors:
            if factor not in factor_set:
                factor_set.add(factor)
                queue.append((factor, move+1))
        
        if N-1 not in factor_set:
            factor_set.add(N-1)
            queue.append((N-1, move+1))  
            
'''    
#有点慢，建了一个庞大的字典，时间和空间都不好= =
N_list = [int(raw_input()) for _ in xrange(Q)]

time.clock()
Max = max(N_list)
sqrt = int(Max ** 0.5) + 1
minmove_list = range(0, Max+1)

for i in xrange(1, Max+1):
    minmove_list[i] = min(minmove_list[i], minmove_list[i-1] + 1)
    
    #for j in xrange(2, min(i, sqrt, Max/i))避免了下面的判断
    for j in xrange(2, sqrt):
        if j > i:
            break
        mul = i * j
        if mul > Max:
            break
        minmove_list[mul] = min(minmove_list[mul], minmove_list[i] + 1)
    
    #重复计算太多，上面的方法直接推出后面的最短路径
    for j in xrange(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            big = i / j
            if minmove_list[big]+1 < minmove_list[i]:
                minmove_list[i] = minmove_list[big] + 1
    
print time.clock()
for N in N_list:
    print minmove_list[N]
'''
'''
递归的方法，太慢了= =
minmove_dict = {0: 0, 1: 1, 2: 2, 3: 3}
def get_minmove(N):
    global minmove_dict

    if N in minmove_dict:
        return minmove_dict[N]
    else:
        factor_list = []
        for i in xrange(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                factor_list.append(N / i)
        factor_list.append(N - 1)
        
        minmove = min(
            [get_minmove(factor) for factor in factor_list]
        ) + 1
        minmove_dict[N] = minmove
        return minmove

for _ in xrange(Q):
    N = int(raw_input())
    
    print get_minmove(N)
    
'''
   
