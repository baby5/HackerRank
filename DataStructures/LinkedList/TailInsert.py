#coding:utf-8

def Insert(head, data):
    if head:
        node = head
        while node.next:
            node = node.next
        node.next = Node(data)
    else:
        head = Node(data)
    return head
