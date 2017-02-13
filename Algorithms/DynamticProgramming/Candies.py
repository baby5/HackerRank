#coding:utf-8

N = int(raw_input())
minimum = 0
prev_n = 0  
prev_r = 0
is_down = False
add_num = 0
down_num = 0
for _ in xrange(N):
    r = int(raw_input())
    n = 0

    if prev_r < r:
        n = prev_n + 1
        is_down = False
        add_num = 0
    elif prev_r == r:
        n = 1
        is_down = False
        add_num = 0
    elif prev_r > r:
        n = 1
        if is_down:
            add_num += 1
        else:
            down_num = prev_n - 1
        if add_num == down_num: add_num += 1
        if prev_n == 1: minimum += add_num
        is_down = True

    minimum += n
    prev_n = n
    prev_r = r

print minimum
