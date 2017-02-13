#coding:utf-8

"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

"""
def print_list_stupid(head):
    if head.data:
        print head.data:
    node = head.next
    while(1):
        if node:
            print node.data
            node = node.next
        else:
            break

def print_list_smart(head)
    while head:
        print head.data
        head = head.next
