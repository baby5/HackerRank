#coding:utf-8

n = int(raw_input())
ar = map(int, raw_input().split())

ar1 = ar[:]
insert_swaps = 0
for i in xrange(1, n):
    j = i
    key = ar1[i]

    while j > 0 and ar1[j-1] > key:
        ar1[j] = ar1[j-1]
        j -= 1
        insert_swaps += 1

    ar1[j] = key

quick_swaps = 0
def quick_sort(ar, lo, hi):
    global quick_swaps

    if hi > lo:
        p = ar[hi]
        i = lo
        
        for j in xrange(lo, hi):
            if ar[j] < p:
                ar[i], ar[j] = ar[j], ar[i]
                quick_swaps += 1 
                i += 1
                
        ar[i], ar[hi] = ar[hi], ar[i]
        quick_swaps += 1
        quick_sort(ar, lo, i-1)
        quick_sort(ar, i+1, hi)

quick_sort(ar, 0, n-1)
print insert_swaps - quick_swaps
