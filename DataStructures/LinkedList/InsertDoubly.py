#coding:utf-8

def SortedInsert(head, data):
    if head is None:
        return Node(data)
    cur = head
    prev = None
    while 1:
        if cur is None or data < cur.data:
            node = Node(data, cur, prev)
            prev.next = node
            if cur is not None:
                cur.prev = node
            break
        prev = cur
        cur = cur.next
    return head
