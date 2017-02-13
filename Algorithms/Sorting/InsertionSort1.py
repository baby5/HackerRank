#coding:utf-8

size = int(raw_input())
arr = raw_input().split()
e = arr[-1]

for i in xrange(size-1, -1, -1):
    if i == 0 or arr[i-1] <= e:
        arr[i] = e
        print ' '.join(arr)
        break
    else:
        arr[i] = arr[i-1]
        print ' '.join(arr)
    
