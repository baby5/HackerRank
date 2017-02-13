#coding:utf-8

#T = int(raw_input())
T = 1

for _ in xrange(T):
    #s = raw_input()
    s = 'ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'
    length = len(s)
    
    count = 0
    for i in xrange(length):
        dic = {}
        for j in xrange(length-i):
            substr = ''.join(sorted(s[j:j+i+1]))
            dic[substr] = dic.get(substr, 0) + 1

        count += sum(map(lambda x: x*(x-1)/2, dic.values()))
        
    print count
'''
#大神
t = int(raw_input())
for _ in range(t):
    s = raw_input().strip()
    pc = dict()
    n = len(s)
    for i in range(n):
        cx = [0]*26
        for j in range(i,n):
            cx[ord(s[j])-97] += 1
            pc[tuple(cx)] = pc.get(tuple(cx),0)+1
    res = 0
    for x in pc:
        res += pc[x]*(pc[x]-1)/2
    print res
''' 
