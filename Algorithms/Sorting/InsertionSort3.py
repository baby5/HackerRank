#coding:utf-8

N = int(raw_input())
a = map(int, raw_input().split())

count = 0
for i in xrange(1, N):
    x = a[i]
    j = i
    while j > 0 and a[j-1] > x:
        a[j] = a[j-1]
        j -= 1
        count += 1
    a[j] = x

print count
    
