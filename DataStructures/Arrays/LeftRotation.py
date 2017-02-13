#coding:utf-8

n, d = map(int, raw_input().split())
array = raw_input().split()

d = d % n
while(d):
    array.append(array.pop(0))
    d -= 1
print ' '.join(array)
