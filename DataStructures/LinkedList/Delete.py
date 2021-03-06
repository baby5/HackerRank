#coding:utf-8

def Delete(head, position):
    count = 0
    prev = None
    cur = head
    while cur is not None and count < position:
        count += 1
        prev = cur
        cur = cur.next
   
    #make sure input is valid
    if count != position:
        return 0
    else:
        if prev is None:
            return head
        else:
            prev.next = cur.next
            return head
