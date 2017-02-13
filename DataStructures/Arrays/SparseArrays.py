#coding:utf-8

N = int(raw_input())

str_list = []
for _ in range(N):
    str_list.append(raw_input())

Q = int(raw_input())

query_list = []
for _ in range(Q):
    query_list.append(raw_input())

for query in query_list:
    print str_list.count(query)
