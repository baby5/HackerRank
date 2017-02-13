#coding:utf-8

from math import log

for _ in xrange(input()):
    a, b = map(int, raw_input().split())

    an = 0 if a==0 else int(log(a, 2))
    bn = int(log(b, 2))

    if bn > an:
        print 0
    elif bn == an:
        num_str = str(bin(a))
        length = len(str(bin(a^b))) - 2

        new_num = num_str[:-length] + '0'*length
        print eval(new_num)

        
