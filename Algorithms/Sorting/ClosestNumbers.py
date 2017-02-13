#coding:utf-8

N = int(raw_input())
ar = map(int, raw_input().split())

def insert_sort(ar):
    for i in xrange(N):
        key = ar[i]
        j = i
        while j > 0 and ar[j-1] > key:
            ar[j] = ar[j-1]
            j -= 1
        ar[j] = key
    return ar

def quick_sort(ar, lo, hi):
    if hi > lo:
        pivot = ar[lo]
        i = lo
        j = hi

        while 1:
            while ar[i] < pivot:
                i += 1
            while ar[j] > pivot:
                j -= 1
        
            if i >= j:
                break

            ar[i], ar[j] = ar[j], ar[i]

        ar[j] = pivot
        quick_sort(ar, lo, j-1)
        quick_sort(ar, j+1, hi)

ar.sort()
stack = ar[0:2]
diff = ar[1] - ar[0]
for i in xrange(1, N):
    if ar[i] - ar[i-1] < diff:
        stack = ar[i-1:i+1]
        diff = ar[i] - ar[i-1]
    elif ar[i] - ar[i-1] == diff:
        stack += ar[i-1:i+1]

print ' '.join(map(str, stack))
