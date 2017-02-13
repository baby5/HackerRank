#coding:utf-8

N = int(raw_input())
string = raw_input()

prev = None
chr_set = set()
del_set = set()
for char in string:
    if char != prev and char not in del_set:
        chr_set.add(char)
    elif char == prev and char in chr_set:
        chr_set.remove(char)
        del_set.add(char)
    prev = char

def get_t_length(chr_tuple):
    prev = None
    count = 0
    for char in string:
        if char in chr_tuple:
            if char == prev:
                return 0
            prev = char
            count += 1
    return count

size = len(chr_set)
if size <= 1:
    print 0
else:
    from itertools import combinations
    maximum = 0
    for pair in combinations(chr_set, 2):
        maximum = max(maximum, get_t_length(pair))
    print maximum

