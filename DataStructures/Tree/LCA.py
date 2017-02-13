#coding:utf-8

def lca(root, v1, v2):
    while 1:
        if v1 < root.data and v2 < root.data:
            root = root.left
        elif v1 > root.data and v2 > root.data:
            root = root.right
        else:
            return root

def lca_recu(root, v1, v2):
    if root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)
    if root.data > v1 and root.data > v2:
        return lca(root.left, v1, v2)
    return root
