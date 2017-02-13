#coding:utf-8

def find(disjoin_set, i):
    if disjoin_set[i] <= -1:
        return i
    else:
        disjoin_set[i] = find(disjoin_set, disjoin_set[i])
        return disjoin_set[i]

N, Q = map(int, raw_input().split())

disjoin_set = [-1] * (N+1)

for _ in xrange(Q):
    s = raw_input()

    if s.startswith('Q'):
        i = int(s.split()[1])
   
        #递归路径压缩
        i = find(disjoin_set, i)
        '''
        #循环找根，如果要实现路径压缩，要把所有父节点不为根的节点记录下来，最后统一替换为根节点，因为循环过程中还不知道根节点在哪里。
        while disjoin_set[i] > -1:
            i = disjoin_set[i]
        '''
        print abs(disjoin_set[i])

    elif s.startswith('M'):
        i, j = map(int, s.split()[1:])

        #在union操作中find，可以顺便路径压缩
        i = find(disjoin_set, i)
        j = find(disjoin_set, j)
        '''
        while disjoin_set[i] > -1:
            i = disjoin_set[i]

        while disjoin_set[j] > -1:
            j = disjoin_set[j]
        '''
        if i == j:
            continue    
    
        if abs(disjoin_set[i]) > abs(disjoin_set[j]):
            disjoin_set[i] += disjoin_set[j]
            disjoin_set[j] = i
        else:
            disjoin_set[j] += disjoin_set[i]
            disjoin_set[i] = j
            
