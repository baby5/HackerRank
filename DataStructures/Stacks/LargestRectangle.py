#coding:utf-8
import pdb

N = int(input())
h = map(int, raw_input().split()) + [0]

stack = []
i = 0 #i代表索引，也可间接计算宽度
best = 0
#very smart
while i<=N:
    #如果 空栈 或 前值小于等于当前值
    if len(stack)==0 or h[stack[-1]]<=h[i]:
        stack.append(i)
        i+=1
    else:
        p = stack.pop()
        #如果栈空，则当前i的值即为宽度
        #如果非空，则i - 栈最后一个索引 - 1 = 宽度
        A = h[p]*(i-stack[-1]-1) if len(stack)>0 else h[p]*i
        best = max(best,A)
print best
'''
N = int(raw_input())
h_list = map(int, raw_input().split())

Max = None
for i in xrange(N):
    h = h_list[i]
    count = 1
    j = i
    while j > 0:
        j -= 1
        left = h_list[j]
        if left < h:
            break
        else:
            count += 1
    while i < N-1:
        i += 1
        right = h_list[i]
        if right < h:
            break
        else:
            count += 1
    s = h * count
    if Max != None:
        if s > Max:
            Max = s
    else:
        Max = s

print Max
'''        
    

