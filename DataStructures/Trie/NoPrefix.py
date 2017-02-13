#coding:utf-8

N = int(raw_input())
root = {}

for _ in xrange(N):
    s = raw_input()
    node = root
    is_added = False
    
    if s[0] not in root:
        for char in s:
            node[char] = {}
            node = node[char]
            is_added = True
        continue
    
    is_added = False
    for char in s:
        if len(node) != 0 and char not in node:
            node[char] = {}
            node = node[char]
            is_added = True
        elif len(node) == 0:
            if is_added:
                node[char] = {}
                node = node[char]
            else:
                break
        elif char in node:
            node = node[char]
    
    if not is_added:
        print 'BAD SET'
        print s
        break

if is_added:
    print 'GOOD SET'
'''
#偷懒的解法
N = int(raw_input())

Set = []

for _ in xrange(N):
    s = raw_input()
    end = False

    for string in Set:
        if string.startswith(s) or s.startswith(string): 
            print 'BAD SET'
            print s
            end = True
            break
    
    if end:
        break

    Set.append(s)

if not end:
    print 'GOOD SET'    
'''     
