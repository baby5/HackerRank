#coding:utf-8

def CompareLists(headA, headB):
    mark = 1
    while headA or headB:
        A_data = headA.data if headA else None
        B_data = headB.data if headB else None
        if A_data != B_data:
            mark = 0
            break
        headA = headA.next
        headB = headB.next
    return mark


def CompareLists(headA, headB):
    if headA is None and headB is None:
        return 1
    elif headA is not None and headB is not None:
        if (headA.data != headB.data):
            return 0
    else:
        return 0
    
    return CompareLists(headA.next, headB.next)
