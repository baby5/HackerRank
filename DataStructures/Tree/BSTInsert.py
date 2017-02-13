#coding:utf-8


def insert_iteration(root, value):
    temp = root
    if root is None:
        return Node(value)
    while 1:
        if value < root.data:
            if root.left:
                root = root.left
            else:
                root.left = Node(value)
                break
        else:
            if root.right:
                root = root.right
            else:
                root.right = Node(value)
                break

   return temp

def insert_recursion(root, value):
    if root is None:
        return Node(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
