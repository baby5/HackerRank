#coding:utf-8

from collections import Counter

n = int(raw_input())

c_list = map(int, raw_input().split())

c_dict = Counter(c_list)

pair_num = 0
for key in c_dict:
    pair_num += c_dict[key] / 2

print pair_num
