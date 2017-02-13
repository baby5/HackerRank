#coding:utf-8

N, M = map(int, raw_input().split())

array = [raw_input() for _ in xrange(N)]

maximum = 0
teamnum = 0
for i in xrange(N):
    bin1 = int(array[i], 2)
    for j in xrange(i+1, N):
        bin2 = int(array[j], 2)
        topic_num = bin(bin1|bin2)[2:].count('1')

        if topic_num > maximum:
            maximum = topic_num
            teamnum = 1
        elif topic_num == maximum:
            teamnum += 1
        
print maximum
print teamnum
