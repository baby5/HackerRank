#coding:utf-8

n, k = map(int, raw_input().split())
ar = sorted(map(int, raw_input().split()))

count = 0
pos = None
pre = None
for i in xrange(n):
    if pos == None and pre == None:
        pre = ar[i]
        if i == n-1:
            count += 1
    elif pos == None:
        dis = abs(ar[i] - pre)
        if dis == k:
            pos = ar[i]
            count += 1
        elif dis > k:
            pre = ar[i]
            count += 1
            if i == n-1:
                count += 1
        elif dis < k:
            if i != n-1 and abs(ar[i+1]-pre) > k:
                pos = ar[i]
                count += 1
            if i == n-1:
                count += 1
    else:
        dis = abs(ar[i] - pos)
        if dis > k:
            if i == n-1:
                count += 1
            else:
                pos = None
                pre = ar[i]
print count