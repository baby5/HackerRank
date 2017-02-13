def Insert_stupid(head, data):
    if head:
        return Node(data, head)
    else:
        return Node(data)

def Insert_smart(head, data):
    return Node(data, head)
