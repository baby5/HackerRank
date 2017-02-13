#coding:utf-8

N, M = map(int, raw_input().split())

array = raw_input().split()

for _ in range(M):
    t, i, j = map(int, raw_input().split())
    s = slice(i-1, j)
    array_slice = array[s]
    del array[s]
    if t == 1:
        array = array_slice + array
    elif t == 2:
        array = array + array_slice

print array[0] - array[-1]
print ' '.join(array)
