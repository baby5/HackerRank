#coding:utf-8

N = int(raw_input())

A = map(int, raw_input().split())

stack = []
Max = 0
for a in A:
    while stack and a <= stack[-1]:
        Max = max(Max, stack.pop() ^ a)
    
    if stack != []:
        Max = max(Max, stack[-1] ^ a) 
    stack.append(a)

print Max
