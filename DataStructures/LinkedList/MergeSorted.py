#coding:utf-8

def MergeLists_very_smart(headA, headB):
    if headA == None:
        return headB
    if headB == None:
        return headA
    
    if headA.data < headB.data:
        headA.next = MergeLists(headA.next, headB)
        return headA
    else:
        headB.next = MergeLists(headA, headB.next)
        return headB
    
