#coding:utf-8

N = int(raw_input())

S = ''
stack = [S]
for _ in xrange(N):
    s = raw_input()
    if s.startswith('1'):
        S = ''.join((S, s.split()[-1]))
        stack.append(S)
    elif s.startswith('2'):
        k = int(s.split()[-1])
        S = S[:-k]
        stack.append(S)
    elif s.startswith('3'):
        k = int(s.split()[-1])
        index = k-1
        print S[index]
    elif s.startswith('4'):
        stack.pop()
        S = stack[-1]
        
