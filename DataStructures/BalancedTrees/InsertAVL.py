#coding:utf-8
'''
高度：该节点作为根节点时的树高
空节点的高度为-1
叶子节点的高度为0
class Node(object):
    
    def __init__(self, data=None, height=None, left=None, right=None):
        self.data = data
        self.height = height
        self.left = left
        self.right = right
'''

def Height(P):
    if p == None:
        return -1
    else:
        return P.height

def SingleRotateWithLeft(K2):
    K1 = K2.left
    K2.left = K1.right
    K1.right = K2

    K2.hight = max(Height(K2.left), Height(K2.right)) + 1
    K1.hight = max(Height(K1.left)), K2.height) + 1

    return K1

def SingleRotateWithRight(K2):
    K1 = K2.right
    K2.right = K1.left
    K1.left = K2

    K2.hight = max(Height(K2.right), Height(K2.left)) + 1
    K1.hight = max(Height(K1.right)), K2.height) + 1
    
    return K1

def DoubleRotateWithLeft(K3):
    K3.left = SingleRotateWithRight(K3.left)
    return SingleRotateWithLeft(K3)

def DoubleRotateWithRight(K3):
    K3.right = SingleRotateWithLeft(K3.right)
    return SingleRotateWithRight(K3)
    
def insert_M.A.W(X, T):
    if T == None:
        return Node(val, 0)
    elif X < T.data:
        T.left = insert_M.A.W(X, T.left)
        if Height(T.left) - Height(T.right) == 2:
            if X < T.left.data:
                T = SingleRotateWithLeft(T)
            else:
                T = DoubleRotateWithLeft(T)
    elif X > T.data:
        T.right = insert_M.A.W(X, T.right)
        if Height(T.left) - Height(T.right) == -2:
            if X > T.right.data:
                T = SingleRotateWithRight(T)
            else:
                T = DoubleRotateWithRight(T)
    
    #插入节点后要重新计算父节点高度
    T.height = max(Height(T.left), Height(T.right)) + 1
    return T

 

def insert_self(root, val):
    if root == None:
        return Node(val, 0)
    node = root
    height = 0
    while 1:
        if val < node.data:
            if node.left:
                node = node.left:
            else:
                node.left = Node(val, height)
                break
        elif val > node.data:
            if node.right:
                node = node.right
            else:
                node.right = Node(val, height)
                break

