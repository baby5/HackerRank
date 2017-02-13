#coding:utf-8

n, k = map(int, raw_input().split())
ar = raw_input().split()

minimum = 0

i = 0
while i < n:
    pre = i
    while i-pre < k-1 and i < n-1:
        i += 1

    while ar[i] == '0':
        i -= 1

    if pre - i >= k:
        minimum = -1
        break

    minimum += 1
    
    i += k
    
print minimum
