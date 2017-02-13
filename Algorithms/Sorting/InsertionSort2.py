#coding:utf-8

s = int(raw_input())
ar = map(int, raw_input().split())

for i in xrange(1, s):
    if ar[i] < ar[i-1]:
        x = ar[i]
        j = i
        while j > 0 and x < ar[j-1]:
            ar[j] = ar[j-1]
            #ar[j], ar[j-1] = ar[j-1], ar[j]
            j -= 1
        ar[j] = x
        
    print ' '.join(map(str, ar))
