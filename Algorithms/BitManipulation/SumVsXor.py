#coding:utf-8

from math import factorial as fl
N = input()
if N == 0:
    print 1
else:
    n = str(bin(N)).count('0') - 1
    print 2 ** n
