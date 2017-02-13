#coding:utf-8

def height(root):
    height = 0
    prev_list = []
    cur_list = [root]
    while 1:
        prev_list = cur_list
        cur_list = []
        for node in prev_list:
            if node.left:
                cur_list.append(node.left)
            if node.right:
                cur_list.append(node.right)
        if not prev_list:
            break
        height += 1
    return height
        
def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root,left), height(root.right)) 
