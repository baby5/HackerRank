#coding:utf-8

def inOrder(root):
    if root:
        inOrder(root.left)
        print root.data,
        inOrder(root.right)


def inOrder_stupid(root):
    stack = [root]

    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node)
            stack.append(node.left)
            node.left = None
        elif node.right:
            stack.append(node.right)
            stack.append(node)
            node.right = None
        else:
            print node.data,

def inOrder_smart(root):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print root.data,
        root = root.right

