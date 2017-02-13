#coding:utf-8

n = int(raw_input())

ar = [(i, sum(map(int, raw_input().split()))) for i in xrange(1, n+1)]

ar.sort(key=lambda x: x[1])
print ' '.join(map(str, [a[0] for a in ar]))
