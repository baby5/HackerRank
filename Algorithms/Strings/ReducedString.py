#coding:utf-8

S = list(raw_input())
stack = []

for char in S:
    if stack == []:
        stack.append(char)
    else:
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

if stack == []:
    print 'Empty String'
else:
    print ''.join(stack)

'''
while 1:
    string = ''
    N = len(S)
    is_reduced = False

    i = 0
    while i <= N-1:
        if i+1 < N and S[i] == S[i+1]:
            i += 2
            is_reduced = True
        else:
            string += S[i] 
            i += 1
    if not is_reduced:
        break
    S = string

if S == '':
    print 'Empty String'
else:
    print S
'''    

