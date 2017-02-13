#coding:utf-8

def FindMergeNode(headA, headB):
    temp = headB
    while headA:
        headB = temp
        while headB:
            if headA.next is headB.next and headA.next:
                return headA.next.data
            headB = headB.next
        headA = headA.next

def FindMergeNode_smart(headA, headB):
    curA = headA
    curB = headB
    while curA is not curB:
        if curA.next is None:
            curA = headB
        else:
            curA = cruA.next
        if curB.next is None:
            curB = heaA
        else:
            curB = cruB.next
    return curA.data
