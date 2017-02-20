#coding:utf-8

#smart
def MergeLists(headA, headB):
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
    
