# coding:utf-8

n = int(raw_input())
ar = map(int, raw_input().split())

p = ar[0]
left = []
equal = [p]
right = []

for x in ar[1:]:
    if x < p:
        left.append(x)
    else:
        right.append(x)

print ' '.join(map(str, left+equal+right))
