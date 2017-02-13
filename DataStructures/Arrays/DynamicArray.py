#coding:utf-8

#N, Q = map(int, raw_input().split(' '))
with open('input', 'r') as fIn:
    lines = fIn.readlines()
    N, Q = map(int, lines[0].strip().split(' '))

lastAns = 0
seqList = [[] for i in xrange(N)]

#input_list = []
#for i in xrange(Q):
#    input_list.append(raw_input())

for query_str in lines[1:]:
    type_num, x, y = map(int, query_str.split(' '))
    index = (x ^ lastAns) % N
    if type_num == 1:
        seqList[index].append(y)
    elif type_num == 2:
        seq = seqList[index]
        lastAns = seq[y % len(seq)]
        print lastAns
