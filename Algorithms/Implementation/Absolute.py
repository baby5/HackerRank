# coding:utf-8

from itertools import permutations

T = int(raw_input())

for _ in xrange(T):
    N, K = map(int, raw_input().split())

    if N % 2 != 0:
        if K == 0:
            print ' '.join(map(str, xrange(1, N+1)))
        else:
            print -1
    else:
        if K == 0:
            print ' '.join(map(str, xrange(1, N+1)))
        elif N % K == 0 and N/K % 2 == 0:
            step = 2 * K
            time = N / step
            num_list = range(1, N+1)

            for i in xrange(time):
                start = i * step
                end = (i+1) * step
                mid = start + K

                num_list[start:mid], num_list[mid:end] = (
                    num_list[mid:end], num_list[start:mid]
                )

            print ' '.join(map(str, num_list))
        else:
            print -1
'''
#全排列太慢了
for _ in xrange(T):
    N, K = map(int, raw_input().split())

    p_list = permutations(xrange(1,N+1), N)

    is_exist = False
    for p in p_list:
        is_abs = True
        for i in xrange(1, N+1):
            if abs(p[i-1] - i) != K:
                is_abs = False

        if is_abs:
            print ' '.join(map(str, p))
            is_exist = True
            break

    if not is_exist:
        print -1
'''
