#coding:utf-8

#较好的思路：
#先排序，找出不相等的索引，
#如果没有则不用操作，
#如果只有两个则swap，
#如果多个，就找最小和最大的索引，将之间的反转，判断反转后是否是增序
#都不行，print no
n = int(raw_input())

d_list = map(int, raw_input().split())

dl = None
dr = None
operation = None

pre = d_list[0]
size = len(d_list)
for i in xrange(size):
    
    if dl == None:
        if d_list[i] < pre:
            dl = i - 1
    elif dr == None:
        if d_list[i] > d_list[dl]:
            dr = i - 1
        elif i == size-1:
            dr = i
    else:
        break
    
    pre = d_list[i]

dr = i if dr == None else dr

def is_sorted(array):
    pre = array[0]
    for term in array[1:]:
        if term < pre:
            return False
        pre = term
    return True

if len(d_list[dl:dr+1]) <= 3:
    d_list[dl], d_list[dr] = d_list[dr], d_list[dl]
    if is_sorted(d_list):
        print 'yes'
        print 'swap %d %d' % (dl+1, dr+1)
    else:
        print 'no'
else:
    if d_list[dl+1] < d_list[dl+2]:
        d_list[dl], d_list[dr] = d_list[dr], d_list[dl]
        if is_sorted(d_list):
            print 'yes'
            print 'swap %d %d' % (dl+1, dr+1)
        else:
            print 'no'
    else:
        d_list[dl: dr+1] = d_list[dl: dr+1][::-1]
        if is_sorted(d_list):
            print 'yes'
            print 'reverse %d %d' % (dl+1, dr+1)
        else:
            print 'no'
        
