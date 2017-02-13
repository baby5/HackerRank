#coding:utf-8

q = int(raw_input())

for _ in xrange(q):
    m, n = map(int, raw_input().split())
    cys = sorted(map(int, raw_input().split()))
    cxs = sorted(map(int, raw_input().split()))
    
    seg_x = 1
    seg_y = 1
    total_cost = 0
    while cys or cxs:
        if cys and cxs:
            if cys[-1] >= cxs[-1]:
                seg = seg_y
                cost = cys.pop()
                seg_x += 1
            else:
                seg = seg_x
                cost = cxs.pop()
                seg_y += 1
        elif cys:
            seg = seg_y
            cost = cys.pop()
        elif cxs:
            seg = seg_x
            cost = cxs.pop()
    
        total_cost += cost * seg
    
    print total_cost % (10**9 + 7)
