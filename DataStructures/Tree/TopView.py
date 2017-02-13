#coding:utf-8

def top_view(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node)
            stack.append(node.left)
            node.left = None
        else:
            print node.data,
    while root.right:
        print root.right.data,

count = 0
def top_view(root):
    global count
    if root.left and count >= 0:
        count += 1
        top_view(root.left)
    
    print root.data
    count -= 1

    if root.right and count < 0:
        count -= 1
        top_view(root.right)

def top_view_smart(root):
    if root.left:
        root.left.right = None
        top_view(root.left)

    print root.data,
    
    if root.right:
        root.right.left = None
        top_view(root.right)


