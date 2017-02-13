#coding:utf-8

N = int(raw_input())

a_list = map(int, raw_input().split())

a_list.sort()

#聪明
print N
for i in xrange(1, N):
    if a_list[i] == a_list[i-1]:
        continue
    print N - i
'''
while a_list:
    print len(a_list) 
    a_list = map(lambda x: x-a_list[0], a_list)
   
    count = 0
    for a in a_list:
        if a == 0:
            count += 1
        else:
            break

    a_list = a_list[count:]
'''
