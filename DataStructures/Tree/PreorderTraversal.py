#coding:utf-8

def preOrder(root):    
    print root.data,
    if root.left is not None:
        preOrder(root.left)
    if root.right is not None:
        preOrder(root.right)
    
def preOrder_smart(root):
    if root != None:
        print root.data,
        preOrder(root.left)
        preOrder(root.right)

def preOrder_loop(root):
    stack = [root]

    while stack:
        node = stack.pop()
        print node.data,
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

