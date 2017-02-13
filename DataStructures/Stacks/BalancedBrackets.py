#coding:utf-8

n = int(raw_input())

pair = {
    '(': ')',
    '[': ']',
    '{': '}',
}
for _ in xrange(n):
    s = raw_input()
    stacks = []
    length = len(s)
    if length % 2 != 0:
        print 'NO'
        break
    mark = True
    for i in xrange(length):
        char = s[i]
        if char in pair:
            stacks.append(char)
        else:
            if stacks != []:
                item = stacks.pop()
                if pair[item] != char:
                    mark = False
                    break
            else:
                mark = False
                break
    if i == length-1 and stacks != []:
        mark = False

    if mark:
        print 'YES'
    else:
        print 'NO'

#Black Box用return来操作
def judge(s):
    stack = []
    for c in s:
        if c in pair:
            stack.append(c)
        elif not stack or stack.pop() != pair(c):
            return False
    return not stack            
