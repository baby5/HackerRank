#coding:utf-8

T = int(raw_input())

for _ in xrange(T):
    n, a, b = (int(raw_input()) for _ in xrange(3))

    if a == b:
        print a*(n-1)
        continue

    i = n-1
    array = []
    a, b = min(a, b), max(a, b)
    while i >= 0:
        store = 0
        store += i*a
        store += (n-1-i)*b
        array.append(str(store))
        i -= 1

    print ' '.join(array)
