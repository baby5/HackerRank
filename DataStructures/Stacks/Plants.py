#coding:utf-8

#构造植物类，保存天数
class Plant:
    def __init__(self, pesticide, days):
        self.pesticide = pesticide
        self.days = days
    
def solvePlants(a):
    stack = []
    maxDaysAlive = 0
     
    for pesticide in a:
        #初始化daysAlive
        daysAlive = 0
        #精华，用栈来控制数据行为
        while stack and pesticide <= stack[-1].pesticide:
            daysAlive = max(daysAlive, stack.pop().days)
        
        #栈空，说明数据为降序，右边小于左边，不存在植物死亡
        if not stack:
            daysAlive = 0
        #栈非空，则要多一天来处理数据，所以++
        else:
            daysAlive += 1
        
        #更新最大存活天数
        maxDaysAlive = max(maxDaysAlive, daysAlive)
        #可能存活的植物进栈 
        stack.append(Plant(pesticide, daysAlive))
     
    print maxDaysAlive
    
N = input()
      
numbers = map(int, raw_input().split())
      
solvePlants(numbers)

'''
#未考虑2 11 5 10 9 12 的类似情况
#实际2天
#下列算法输出3天
N = int(raw_input())

P = map(int, raw_input().split())

day = 0
Min = P[0]
prev = Min
add = False
temp_min = None
for p in P[1:]:
    if p <= Min:
        Min = p
    else:
        if p > prev and not add:
            day += 1
            add = True
        elif p <= prev:
            if temp_min == None:
                temp_min = p
                day += 1
            else:
                if p <= temp_min:
                    day += 1
                    temp_min = p
                
    prev = p
print day

#time out
N = int(raw_input())

P = map(int, raw_input().split())

day = 1
while 1:
    if P == []:
        break
    die_list = []
    for i, p in enumerate(P[1:], 1):
        if p > P[i-1]:
            die_list.append(i)
    
    if die_list == []:
        break
    
    n = 0
    for j in die_list:
        P.pop(j-n)
        n += 1
    day += 1

    if P == []:
        break
    die_num = 0
    live_stack = [P[0]]
    prev = P[0]
    
    for p in P[1:]:
        if p > prev:
            die_num += 1
        else:
            live_stack.append(p)
        prev = p
    
    if die_num == 0:
        break
    P = live_stack
    day += 1
'''

