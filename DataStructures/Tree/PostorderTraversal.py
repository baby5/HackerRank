#coding:utf-8

def postOrder(root):
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print root.data,

def postOrder(root):
    stack = [root]
    
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node)
            stack.append(node.left)
            node.left = None
        elif node.right:
            stack.append(node)
            stack.append(node.right)
            node.right = None
        else:
            print node.data,
