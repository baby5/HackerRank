#coding:utf-8

N = int(raw_input())
root = {}

for _ in xrange(N):
    s = raw_input()
    node = root

    if s.startswith('add'):
        for char in s.split()[-1]:
   
            if char not in node:
                node[char] = {'freq': 1}
                node = node[char]
            else:
                node[char]['freq'] += 1
                node = node[char]
    elif s.startswith('find'):
        miss = False
        for char in s.split()[-1]:
            
            if char in node:
                node = node[char]
            else:
                miss = True

        if miss:
            print 0
        else:
            print node['freq']
                    
'''
#一个节点*26，节点多了内存就爆了
class Node(object):
    
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.childNode = [None] * 26

N = int(raw_input())
root = Node()

for _ in xrange(N):
    s = raw_input()
    node = root

    if s.startswith('add'):
        for char in s.split()[-1]:
            i = ord(char) - ord('a')
            
            if node.childNode[i] == None:
                node.childNode[i] = Node(char, 1)
                node = node.childNode[i]
            else:
                node = node.childNode[i]
                node.freq += 1

    elif s.startswith('find'):
        for char in s.split()[-1]:
            i = ord(char) - ord('a')

            node = node.childNode[i]
            if node == None:
                break
        
        if node == None:
            print 0
        else:
            print node.freq
'''
