#coding:utf-8

def find(disjoin_set, i):
    if disjoin_set[i] <= -1:
        return i
    else:
        disjoin_set[i] = find(disjoin_set, disjoin_set[i])
        return disjoin_set[i]

N = int(raw_input())

disjoin_set = [-1] * (2*N + 1)
for _ in xrange(N):
    G, B = map(int, raw_input().split())
    
    G = find(disjoin_set, G)
    B = find(disjoin_set, B) 
    '''
    while disjoin_set[G] > -1:
        G = disjoin_set[G]

    while disjoin_set[B] > -1:
        B = disjoin_set[B]
    '''
    if G == B:
        continue

    disjoin_set[G] += disjoin_set[B]
    disjoin_set[B] = G

component_list = [
    abs(size) for size in disjoin_set if size < -1
]

print min(component_list), max(component_list)
