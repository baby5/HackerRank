#coding:utf-8

def LevelOrder_iteration(root):
    prev_level = []
    cur_level = [root] if root else []   
    while 1:
        prev_level = cur_level
        cur_level = []
        for node in prev_level:
            print node.data,
            if node.left:
                cur_level.append(node)
            if node.right:
                cur_level.append(node)
        if not prev_level:
            break

def LevelOrder_queues(root):
    queues = [root]
    while queues:
        note = queues.pop[0]
        print note.data
        if note.left:
            queues.append(note.left)
        if note.right:
            queues.append(note.right)

