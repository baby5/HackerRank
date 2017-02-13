#coding:utf-8

def RemoveDuplicates(head):
    if head == None:
        return head
    node = head.next
    prev = head
    while node:
        if node.data == prev.data:
            prev.next = node.next
        else:
            prev = node
        node = node.next
    return head
