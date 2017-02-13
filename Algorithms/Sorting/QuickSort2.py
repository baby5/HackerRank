#coding:utf-8

n = int(raw_input())
ar = map(int, raw_input().split())

def quick_sort(ar):
    if len(ar) <= 1:
        return ar
    p = ar[0]
    equal = [p]
    left = []
    right = []

    for x in ar[1:]:
        if x < p:
            left.append(x)
        else:
            right.append(x)

    left1 = quick_sort(left)
    right1 = quick_sort(right)
    
    print ' '.join(map(str, left1+equal+right1))
    return left1 + equal + right1    

quick_sort(ar)
