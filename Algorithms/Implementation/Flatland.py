#coding:utf-8

n, m = map(int, raw_input().split())

c_list = sorted(map(int, raw_input().split()))

cur = 0
pre_value = None
dis_list = []
for i in xrange(n):
    
    if cur == m:
        dis_list.append(i - pre_value)
    elif i < c_list[cur] and pre_value == None:
        cur_value = c_list[cur]
        dis_list.append(cur_value - i)
    elif i == c_list[cur]:
        cur_value = c_list[cur]
        dis_list.append(cur_value - i)
        pre_value = cur_value
        cur += 1
    elif i < c_list[cur] and pre_value != None:
        cur_value = c_list[cur]
        dis_list.append(min(i-pre_value, cur_value-i))

print max(dis_list)
