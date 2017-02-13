#coding:utf-8

from collections import Counter

S = raw_input()
counter = Counter(S)

dic = dict()
for value in counter.values():
    dic[value] = dic.get(value, 0) + 1

size = len(dic)
if size > 2:
    print 'NO'
elif size == 1:
    print 'YES'
else:
    if dic.get(1) == 1:
        print 'YES'
    elif dic.get(min(dic.keys())+1) == 1:
        print 'YES'
    else:
        print 'NO'
        
