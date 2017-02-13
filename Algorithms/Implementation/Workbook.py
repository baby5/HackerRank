#coding:utf-8

n, k = map(int, raw_input().split())

t_list = map(int, raw_input().split())

page = 0
count = 0
for t in t_list:
    page_num = t/k if t%k == 0 else t/k + 1
    
    for i in xrange(1, page_num+1):
        page += 1
        
        t_scope_min = (i-1) * k + 1 
        if i < page_num:
            t_scope_max = i * k
        else:
            t_scope_max = t

        if page >= t_scope_min and page <= t_scope_max:
            count += 1   

print count 
