#coding:utf-8

def InsertNth_stupid(head, data, position):
    if head:
        if position == 0:
            return Node(data, head)
        node = head
        position -= 1
        while position:
            node = node.next
            position -= 1
        node.next = Node(data, node.next)
    else:
        head = Node(data)
    return head
    
def InsertNth_smart(head, data, position):
    count = 0
    prev = None
    cur = head
    while cur is not None and count<position:
        count += 1
        prev = cur
        cur = cur.next

    if prev is None:
        return Node(data, head)
    else:
        prev.next = Node(data, cur)
        return head
