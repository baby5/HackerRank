#coding:utf-8

def get_value(i):
    if i % 4 == 0: return i
    if i % 4 == 1: return 1
    if i % 4 == 2: return i + 1
    if i % 4 == 3: return 0

for _ in xrange(input()):
    l, r = map(int, raw_input().split())

    num_of_2 = r/4 - l/4 - 1
    mid = 0 if num_of_2%2 == 0 else 2

    lam = lambda x,y: x^y
    print reduce(lam, [get_value(i) for i in xrange(l, (l/4+1)*4)]) ^ mid ^ reduce(lam, [get_value(i) for i in xrange((r/4)*4, r+1)])
