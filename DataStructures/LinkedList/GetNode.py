#coding:utf-8

#stupid
def GetNode(head, position):
    prev = None
    node = head
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    
    cur = node
    while position:
        cur = cur.next
        position -= 1
    return cur.data

def GetNode_smart(head, position):
    ptr1 = head
    ptr2 = head
    count = 0
    while ptr1 != None and count < position:
        ptr1 = ptr1.next
        count += 1
    
    while ptr1.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr2.data

def GetNode_smart_two(head, position):
    ptr1 = head
    ptr2 = head
    count = 0
    while ptr1.next != None:
        ptr1 = ptr1.next
        count += 1
        if count > position:
            ptr2 = ptr2.next
    return ptr2.data
