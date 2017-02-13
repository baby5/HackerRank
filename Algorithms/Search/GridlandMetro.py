#coding:utf-8

from collections import defaultdict

n, m, k = map(int, raw_input().split())

track_dic = defaultdict(list)
for _ in xrange(k):
    r, c1, c2 = map(int, raw_input().split())
    track_dic[r].append((c1, c2))

track_count = 0
for track_ar in track_dic.values():
    track_ar.sort(key=lambda x: x[0])

    pre = track_ar[0]
    for i in xrange(1, len(track_ar)):
        cur = track_ar[i]
        if cur[0] > pre[1]:
            track_count += pre[1] - pre[0] + 1
            pre = cur
        else:
            pre = (pre[0], max(pre[1], cur[1]))

    track_count += pre[1] - pre[0] + 1

print n*m - track_count