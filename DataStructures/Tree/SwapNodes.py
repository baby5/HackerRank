#coding:utf-8

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
'''
def Inorder(root):
    if root:
        Inorder(root.left)
        print root.data,
        Inorder(root.right)
'''
def Inorder(root):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print root.data,
        root = root.right

root = Node(1)
N = int(raw_input())
node_list = [root]
for i in range(1, N+1):
    a, b = map(int, raw_input().split())
    node = node_list.pop(0)
    if a != -1:
        node.left = Node(a)
        node_list.append(node.left)
    if b != -1:
        node.right = Node(b)
        node_list.append(node.right)

T = int(raw_input())
K_list = []
for j in range(T):
    K_list.append(int(raw_input()))
 
for K in K_list:    
    prev_list = []
    cur_list = [root]
    swap_list = []
    depth = 1
    while 1:
        if depth%K == 0:
            swap_list.extend(cur_list)
        for node in cur_list:
            if node.left:
                prev_list.append(node.left)
            if node.right:
                prev_list.append(node.right)
        if not prev_list:
            break
        cur_list = prev_list
        prev_list = []
        depth += 1
    for node in swap_list:
        node.left, node.right = node.right, node.left
    Inorder(root)
    print

    
    
