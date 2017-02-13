#coding:utf-8

#n1, n2, n3 = map(int, raw_input().split())
with open('data', 'r') as fIn:
    lines = map(lambda x: x.strip(), fIn.readlines())

#stack1 = map(int, raw_input().split())
stack1 = map(int, lines[0].split())
h1 = sum(stack1)

#stack2 = map(int, raw_input().split())
stack2 = map(int, lines[1].split())
h2 = sum(stack2)

#stack3 = map(int, raw_input().split())
stack3 = map(int, lines[2].split())
h3 = sum(stack3)

while h1 != h2 or h1 != h3:
    if h1 >= h2 and h1 >= h3:
        temp = stack1.pop(0)
        h1 -= temp
    elif h2 >= h1 and h2 >= h3:
        temp = stack2.pop(0)
        h2 -= temp
    elif h3 >= h1 and h3 >= h2:
        temp = stack3.pop(0)
        h3 -= temp

print h1
