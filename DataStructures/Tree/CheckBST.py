#coding:utf-8

def checkBST(root):
    stack = []
    prev = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        
        if prev == None:
            prev = root.data
        else:
            if root.data <= prev:
                return False
            else:
                prev = root.data
        
        root = root.right
    return True   
                
