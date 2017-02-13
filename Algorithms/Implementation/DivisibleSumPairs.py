#coding:utf-8

from itertools import combinations

n, k = map(int, raw_input().split())

a_list = map(int, raw_input().split())

comb_list = combinations(xrange(n), 2)

count = 0
for comb in comb_list:
    if (a_list[comb[0]] + a_list[comb[1]]) % k == 0:
        count += 1

print count
