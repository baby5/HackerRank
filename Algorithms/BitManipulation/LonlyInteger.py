#coding:utf-8

n = int(raw_input())
print reduce(lambda x,y: x ^ y, map(int, raw_input().split()))