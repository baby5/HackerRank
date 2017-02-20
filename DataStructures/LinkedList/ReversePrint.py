#coding:utf-8

def ReversePrint(head):
    data_list = []
    node = head
    while node.next:
        data_list.append(node.data)
        node = node.next
    for data in data_list[::-1]:
        print data

#smart
def ReversePrint(head):
    if head is None:
        return
    ReversePrint(head.next)
    print head.data
