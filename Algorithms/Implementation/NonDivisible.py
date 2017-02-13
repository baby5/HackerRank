#coding:utf-8

n, k = map(int, raw_input().split())

a_list = map(int, raw_input().split())

mod_dict = {}
for a in a_list:
    mod = a % k
    
    if mod in mod_dict:
        mod_dict[mod] += 1
    else:
        mod_dict[mod] = 1

max_size = 0
if 0 in mod_dict:
    max_size = 1
    del mod_dict[0]

half = k/2 + 1
for i in xrange(1, half):
    if i in mod_dict and k-i in mod_dict and i != k-i:
        max_size += max(mod_dict[i], mod_dict[k-i])
    elif k-i in mod_dict and i != k-i:
        max_size += mod_dict[k-i]
    elif i in mod_dict and i != k-i:
        max_size += mod_dict[i]

if k%2 == 0 and k/2 in mod_dict:
    max_size += 1
    
print max_size
    
