#coding:utf-8
import copy

def Reverse(head):
    node = head
    prev = None
    while node:
        temp = copy.deepcopy(node)
        node.next = prev
        prev = node
        node = temp.next
    head = prev
    return heda
