#coding:utf-8

#Puzzle of Fifteen
#https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
#不需要做旋转操作，判断一下'可替换数'的奇偶即可

#并不快= =
T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    a_list = map(int, raw_input().split())
    
    count = 0
    for i in xrange(N):
        for j in xrange(i+1, N):
            count += a_list[i] > a_list[j]

    if count%2 == 0:
        print 'YES'
    else:
        print 'NO'
'''
T = int(raw_input())

def get_L_R(array, array_sort):
    L = None
    for i in xrange(len(a_list)):
        if a_list[i] != a_sort[i]:
            L = i
            break

    R = None
    for i in xrange(len(a_list)-1, -1, -1):
        if a_list[i] != a_sort[i]:
            R = i
            break
    return L, R

for _ in xrange(T):
    N = int(raw_input())
    a_list = map(int, raw_input().split())
    
    a_sort = sorted(a_list)
    if a_list == a_sort:
        print 'YES'
        continue
    
    L, R = get_L_R(a_list, a_sort)
    part = a_list[L: R+1]
    if len(part) == 2:
        print 'NO'
    else:
        while 1: 
            num = L+1
            index = part.index(num)        
           
            #import pdb
            #pdb.set_trace() 
            while index != 0:
                if index == 1:
                    part[index-1: index+2] = [
                        part[index], part[index+1], part[index-1]
                    ]
                    index -= 1
                else:
                    part[index-2: index+1] = [
                        part[index], part[index-2], part[index-1]
                    ]
                    index -= 2
           
            if len(part) == 3:
                if part == sorted(part):
                    print 'YES' 
                else:
                    print 'NO'  
                break  
            
            L = num
            part = part[1:]
'''            
            
