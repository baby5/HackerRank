#coding:utf-8

n = int(raw_input())
ar = map(int, raw_input().split())

def quick_sort_lomuto(ar, low, high):
    if high-low < 1:
        return

    p = ar[high]
    i = low

    for j in xrange(low, high):
        if ar[j] < p:
            ar[j], ar[i] = ar[i], ar[j]
            i += 1
    
    ar[i], ar[high] = p, ar[i]

    print ' '.join(map(str, ar))
    quick_sort(ar, low, i-1)
    quick_sort(ar, i+1, high)


def quick_sort_Hoare(ar, low, high):
    if high > low:
        p = ar[low]
        i = low
        j = high
        while 1:
            while ar[i] < p:
                i += 1
            while ar[j] > p:
                j -= 1
            
            if i >= j:
                break

            ar[i], ar[j] = ar[j], ar[i]
    
        ar[j] = p
        print ' '.join(map(str, ar))
        quick_sort_Hoare(ar, low, j-1)
        quick_sort_Hoare(ar, j+1, high)  

quick_sort_Hoare(ar, 0, n-1)
    
