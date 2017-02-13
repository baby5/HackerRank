#coding:utf-8

def find(disjoin_set, i):
    if disjoin_set[i] <= -1:
        return i
    else:
        disjoin_set[i] = find(disjoin_set, disjoin_set[i])
        return disjoin_set[i]

N = int(raw_input())

#这一行非常耗时
#sum_num = factorial(N) / (factorial(3)*factorial(N-3))

disjoin_set = [-1] * (N+1)
for _ in xrange(N-1):
    s = raw_input()
    if s.endswith('b'):
        i, j = map(int, s.split()[:-1])

        i = find(disjoin_set, i)
        j = find(disjoin_set, j)

        if i == j: continue

        if disjoin_set[i] < disjoin_set[j]:
            disjoin_set[i] += disjoin_set[j]
            disjoin_set[j] = i
        else:
            disjoin_set[j] += disjoin_set[i]
            disjoin_set[i] = j

size_list = [
    abs(size) for size in disjoin_set[1:] if size <= -1
]

def count(sz):
    sx = sx2 = sx3 = 0
    for x in sz:
        sx += x
        sx2 += x**2
        sx3 += x**3
    print (sx*(sx**2-sx2)/2-(sx2*sx-sx3))/3%(10**9+7)

count(size_list)
'''
#计算组合数花费了很多时间
for size in size_list:
    if size == 1: continue

    combin2 = factorial(size) / (factorial(2)*factorial(size-2))
    sum_num -= combin2 * (N-size)

    if size >= 3:
        combin3 = factorial(size) / (factorial(3)*factorial(size-3))
        sum_num -= combin3

print sum_num % (10**9 + 7)
'''
