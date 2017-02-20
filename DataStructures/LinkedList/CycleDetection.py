#coding:utf-8

def has_cycle(head):
    ptr1 = head
    ptr2 = head
    while ptr2 and ptr1.next:
        ptr1 = ptr1.next.next
        ptr2 = ptr2.next
        if ptr1 is ptr2:
            return 1
    return 0
