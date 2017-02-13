#coding:utf-8

s = raw_input()
n = int(raw_input())

length = len(s)
i = n / length
mod = n % length

a_num = s.count('a')

print a_num*i + s[:mod].count('a')
