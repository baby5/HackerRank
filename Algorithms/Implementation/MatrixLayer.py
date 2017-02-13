#coding:utf-8

M, N, R = map(int, raw_input().split())
a_list = [raw_input().split() for _ in xrange(M)]


for i in xrange(min(M, N) / 2):
    m, n = M - i, N - i
    array = []
    
    a = b = i
    #right
    while b < n-1:
        array.append(a_list[a][b])
        b += 1
    #down
    while a < m-1:
        array.append(a_list[a][b])
        a += 1
    #left
    while b > i:
        array.append(a_list[a][b])
        b -= 1
    #up
    while a > i:
        array.append(a_list[a][b])
        a -= 1

    index = R % len(array)
    a = b = i
    while b < n-1:
        a_list[a][b] = array[index]
        b += 1
        index = 0 if index+1 == len(array) else index+1
    while a < m-1:
        a_list[a][b] = array[index]
        a += 1
        index = 0 if index+1 == len(array) else index+1
    while b > i:
        a_list[a][b] = array[index]
        b -= 1
        index = 0 if index+1 == len(array) else index+1
    while a > i :
        a_list[a][b] = array[index]
        a -= 1
        index = 0 if index+1 == len(array) else index+1

for row in a_list:
    print ' '.join(row)
             
    
