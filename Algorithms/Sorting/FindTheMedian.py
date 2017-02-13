#coding:utf-8

n = int(raw_input())
ar = map(int, raw_input().split())

def quick_sort(ar, lo, hi):
    if hi > lo:
        p = ar[lo]
        i, j = lo, hi

        while i < j:
            while i < j and ar[j] >= p:
                j -= 1
            ar[i] = ar[j]
            while i < j and ar[i] <= p:
                i += 1
            ar[j] = ar[i]
        '''
        #python的快速排序实现，挺好的，重复参数的也考虑到了，还好记
        while i < j:
            while i < j:
                if ar[i] > ar[j]:
                    ar[i], ar[j] = ar[j], ar[i]
                    break
                j -= 1
            while i < j:
                if ar[i] > ar[j]: 
                    ar[i], ar[j] = ar[j], ar[i]
                    break
                i += 1
        '''
        ar[i] = p
        quick_sort(ar, lo, i)
        quick_sort(ar, i+1, hi)

quick_sort(ar, 0, n-1)
print ar[n/2]
'''
def quick_sort(ar, lo, hi):
    if hi > lo:
        i = lo
        p = ar[hi]

        for j in xrange(lo, hi):
            if ar[j] < p:
                ar[j], ar[i] = ar[i], ar[j]
                i += 1
        ar[i], ar[hi] = ar[hi], ar[i]
        if i == n/2:
            print ar[i]
            return
        elif i > n/2:
            quick_sort(ar, lo, i-1)
        elif i < n/2:
            quick_sort(ar, i+1, hi)
    else:
        print ar[n/2]
        return
        
quick_sort(ar, 0, n-1)    
'''
