#coding:utf-8

#stupid
def Insert(head, data):
    if head:
        node = head
        while node.next:
            node = node.next
        node.next = Node(data)
    else:
        head = Node(data)
    return head

#smart
def Insert(head, data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)
    return head
    
