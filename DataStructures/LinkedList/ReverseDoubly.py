#coding:utf-8

import copy

def Reverse(head):
    cur = head
    prev = None
    while cur:
        cur.next, cur.prev = cur.prev, cur.next
        prev = cur    
        cur = cur.prev
    return prev
