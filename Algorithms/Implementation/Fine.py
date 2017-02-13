#coding:utf-8

Da, Ma, Ya = map(int, raw_input().split())
De, Me, Ye = map(int, raw_input().split())

if Ya > Ye:
    print 10000
elif Ya == Ye and Ma > Me:
    print 500 * (Ma-Me)
elif Ya == Ye and Ma == Me and Da > De:
    print 15 * (Da-De)
else:
    print 0
