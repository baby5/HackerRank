#coding:utf-8

class Node():

    def __init__(self, data=None, Max=None):
        self.data = data
        self.Max = Max

N = int(raw_input())
stacks = []
for _ in range(N):
    input_str = raw_input()
    if input_str.startswith('1'):
        num, x = map(int, input_str.split())
    else:
        num = int(input_str)
    
    if num == 1:
        if stacks == []:
            stacks.append(Node(x, x))
        else:
            if x >= stacks[-1].Max:
                stacks.append(Node(x, x))
            else:
                Max = stacks[-1].Max
                stacks.append(Node(x, Max))
    elif num == 2:
        if stacks != []:
            stacks.pop()
    elif num == 3:
        print stacks[-1].Max
        
'''
取巧的方法，改变了stack插入的数据。
    if num == 1:
        if stacks == []:
            stacks.append(x)
        else:
            #永远保证大的在第一个
            stacks.append(max(x, stacks[-1]))
    elif num == 2:
        if stacks != []:
            stacks.pop()
    elif num == 3:
        #print max(stacks)
        print stacks[-1]
'''


    
