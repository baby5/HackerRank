#coding:utf-8

t = int(raw_input())

for _ in xrange(t):
    w = list(raw_input())
    length = len(w)
   
    change = None
    for i in xrange(length-1, 0, -1):
        if w[i] > w[i-1]:
            change = i - 1
            break

    if change == None:
        print 'no answer'
    else:
        left_list = sorted(w[change+1:])
        for i in xrange(len(left_list)):
            if left_list[i] > w[change]:
                w[change], left_list[i] = left_list[i], w[change]
                break

        print ''.join(w[:change+1] + left_list)
                
        
