#coding:utf-8

def Reverse(head):
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    head = prev
    return head
