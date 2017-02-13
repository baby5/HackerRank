#coding:utf-8

l = int(raw_input())
r = int(raw_input())

p = l ^ r
maxmium = 1
while p:
    p >>= 1
    maxmium <<= 1

print maxmium - 1

'''
maxmium = 0
for i in xrange(l, r+1):
    for j in xrange(i+1, r+1):
        maxmium = max(maxmium, i^j)

print maxmium
'''

