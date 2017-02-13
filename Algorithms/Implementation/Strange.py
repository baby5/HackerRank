#coding:utf-8

t = int(raw_input())

#非常机智的解法
rem = 3
while t > rem:
    t -= rem
    rem *= 2

#t一定比rem小
print rem - t + 1

'''
n = 0
while 1:
    Sum_cur = 3 * (2**n - 1)
    a_fur = 3 * 2**n
    if Sum_cur + a_fur >= t:
        diff = t - Sum_cur
        print a_fur - diff + 1
        break
    n += 1
''' 
