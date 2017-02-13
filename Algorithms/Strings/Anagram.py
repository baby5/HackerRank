
from collections import Counter

T = int(raw_input())

for _ in xrange(T):
    s = raw_input()
    length = len(s)

    if length % 2 != 0:
        print -1
    else:
        left = s[:length/2]
        left_c = Counter(left)
        right = s[length/2:]
        right_c = Counter(right)

        change = length / 2
        for char, num in right_c.items():
            if char in left_c:
                num_l = left_c[char]
                if num_l >= num:
                    change -= num
                else:
                    change -= num_l
        print change            
